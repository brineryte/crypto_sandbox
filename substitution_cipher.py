import random

KEYSPACE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_key(keyspace=KEYSPACE):
    key = {}
    cletters = list(keyspace)
    for c in keyspace:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key


def encrypt(key, message):
    cipher = ""
    for c in message.upper():
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def get_decrypt_key(key):
    d_key = {}
    for k in key:
        d_key[key[k]] = k
    return d_key


# Generate key
key = generate_key()
print("".join(key.values()))
print()

# Encrypt message
message = "Hey there, buddy."
cipher = encrypt(key, message)
print(cipher, end="\n\n")

# Decrypt
decrypt_key = get_decrypt_key(key)
d_message = encrypt(decrypt_key, cipher)
print(d_message)
