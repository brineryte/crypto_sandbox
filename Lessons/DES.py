from pyDes import *


def modify(cipher):
    mod = [0] * len(cipher)
    mod[9] = 1
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


def run_intro_to_des():
    message = "0123456701234567"
    key = "DESCRYPT"
    iv = bytes([1] * 8)
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)

    cipher = k.encrypt(message)
    print("Length of plain text: ", len(message))
    print("Length of cipher: ", len(cipher))
    print("Encrypted: ", cipher[0:8])
    print("Encrypted: ", cipher[8:16])
    print("Encrypted: ", cipher[16:])
    message = k.decrypt(cipher)
    print("Decrypted: ", message)


def run_modifying_des_cipher():
    message = "Give Bob:    10$ and send to him"
    key = "DESCRYPT"
    iv = bytes([0] * 8)
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)

    # Alice sending encrypted message
    cipher = k.encrypt(message)
    print("Length of plain:", len(message))
    print("Length of cipher:", len(cipher))
    print("Encrypted:", cipher)

    # Bob modifying the cipher text
    cipher = modify(cipher)

    # this is the bank decrypting the message
    message = k.decrypt(cipher)
    print("Decrypted:", message)


def run_double_des_example():
    pass


run_double_des_example()
