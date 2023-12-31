import os

def TxtToBin(plaintext):
    binText = ''.join(format(ord(char), '08b') for char in plaintext)
    return binText

def EncXOR(plaintext, key):
    text = TxtToBin(plaintext)
    key = TxtToBin(key)

    # Ensure the key is of the same length as the plaintext
    if len(key) < len(text):
        key = (key * (len(text) // len(key) + 1))[:len(text)]

    # Perform XOR operation
    cyphertext = ''.join(str(int(text[i]) ^ int(key[i])) for i in range(len(text)))
    return cyphertext

flag = "flag{THIS_IS_PLAIN_TEXT}"
key = os.urandom(5).decode('latin-1')

print(EncXOR(flag, key))
