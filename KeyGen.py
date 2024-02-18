import random
from tables import PC1, PC2, shifts
from BitOperations import permute, shift
from Conversions import bin2hex, hex2bin

def generate_key():
    #Generates a random 64 bit key
    key = random.getrandbits(64)
    key = format(key, '0b').zfill(64)
    return bin2hex(key)

def get_sub_keys(key):
    #Uses input of 64 bit hex string and returns a list of 16, 48 bit subkeys in binary representation
    subKeys = []
    key = hex2bin(key)
    key = permute(key, PC1)
    left = key[:28]
    right = key[28:]
    for i in range(16):
        left = shift(left, shifts[i])
        right = shift(right, shifts[i])
        subKeys.append(permute(left + right, PC2))
    return subKeys

if __name__ == "__main__":
    # Print example key and sub_keys
    key = generate_key()
    print("Main encryption key: {}\n".format(key))
    subKeys = get_sub_keys(key)
    print("SubKeys:")
    print(',\n'.join(bin2hex(x) for x in subKeys))