from tables import IP, IP1, E, S, P
from KeyGen import generate_key, get_sub_keys
from BitOperations import permute, xor
from Conversions import bin2hex, hex2bin, hex2text, text2hex

import math

def DES(hex_string, sub_keys):
    #Outer function to limit ability to call inner functions in isolation to simplify public interface
    def create_blocks(bin_text):
        #Split input message into blocks of length 64 bits and right pad wtih zeros if needed
        num_blocks = math.ceil(len(bin_text) / 64)
        padded_bin = bin_text.ljust(64 * num_blocks, str(0))
        blocks = []
        for i in range(0, len(padded_bin), 64):
            blocks.append(padded_bin[i:i+64])
        return blocks
    
    def encrypt_block(block, sub_keys):
        # Runs the DES algorithm on a single 64 bit block of text using the given subkeys
        initial_permutation = permute(block, IP)
        left = initial_permutation[:32]
        right = initial_permutation[32:]
        for i in range(16):
            right_expanded = permute(right, E)
            right_xor = xor(right_expanded, sub_keys[i])
            sbox_str = ''
            for j in range(8):
                row = int(right_xor[j*6] + right_xor[j*6+5], 2)
                col = int(right_xor[j*6+1:j*6+5], 2)
                val = S[j][row][col]
                sbox_str += bin(val)[2:].zfill(4)
            
            sbox_permuted = permute(sbox_str, P)
            result = xor(left, sbox_permuted)
            left = result

            if i != 15:
                left, right = right, left

            
        combined = left + right
        cypher_text = permute(combined, IP1)

        return cypher_text 
    
    # Outer function for splitting the input hex string into 64 bit blocks and running encrypt_block on all blocks
    # and concatinate into a single hex string which can be transmitted
    bin_string = hex2bin(hex_string)
    blocks = create_blocks(bin_string)
    cypher_text = ''
    for block in blocks:
        cypher_text += encrypt_block(block, sub_keys)
    return bin2hex(cypher_text)

def Encrypt(text, key=None):
    # Wrapper function which takes in text, and returns the cyphertext and key used both in hexadecimal representation
    # Optional key parameter for if a known key is desired
    if key is None:
        key = generate_key()
    sub_keys = get_sub_keys(key)
    return (DES(text2hex(text), sub_keys), key)

def Decrypt(cypher, key):
    # Wrapper function which takes in cyphertext and key in hexadecimal representation, and returns the decrypted text in ascii
    sub_keys = get_sub_keys(key)
    sub_keys = sub_keys[::-1]
    return hex2text(DES(cypher, sub_keys).rstrip('0'))


if __name__ == '__main__':
    plaintext = input("Enter text to be encrpyted: ")
    #plaintext = "Hello World!"
    key = generate_key()
    print("Key: {}\n".format(key))
    print("Plaintext ascii: {}".format(plaintext))
    print("Plaintext hexadecimal: {}".format(text2hex(plaintext)))
    encrypted, _ = Encrypt(plaintext, key)
    print("\n--------\n")
    print("Cyphertext: {}".format(encrypted))
    print("\n--------\n")
    decrypted = Decrypt(encrypted, key)
    print("Decrypted hexadecimal: {}".format(text2hex(decrypted)))
    print("Decrypted ascii: {}".format(decrypted))