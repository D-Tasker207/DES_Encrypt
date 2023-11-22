#Utility methods for bit operations

def permute(arr, permutation):
    #Permute the given text using the given permutation
    return ''.join(arr[i-1] for i in permutation)

def shift(text, n):
    #Shift the given text left by n bits
    return text[n:] + text[:n]

def xor(text1, text2):
    #XOR the two given texts
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(text1, text2))