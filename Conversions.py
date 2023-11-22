import math

#Conversions between different representations of text data

def text2hex(text):
    #Convert ascii text to hex representation
    return text.encode('ascii').hex()

def text2bin(text):
    #Convert ascii text to binary representation
    return ''.join([bin(b.encode('ascii')[0])[2:].zfill(8) for b in text])

def bin2hex(bin_string):
    #Convert binary string to hex string representation
    return hex(int(bin_string, 2))[2:]

def hex2bin(hex_string):
    #Convert hex string to binary string representation
    bin_string = bin(int(hex_string, 16))[2:]
    padding = (8 - len(bin_string) % 8) % 8
    return bin_string.zfill(len(bin_string) + padding)

def hex2text(hex_string):
    #Convert hex string to ascii text representation
    return bytes.fromhex(hex_string).decode('ascii')