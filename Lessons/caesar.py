# implement a caesar cipher
import enchant

d = enchant.Dict("en_US")
KEYSPACE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_key(offset, keyspace=KEYSPACE):
    key = {}
    cnt = 0
    for c in keyspace:
        key[c] = keyspace[(cnt + offset) % len(keyspace)]
        cnt += 1
    return key


def encrypt_message(key, message):
    cipher = ''
    for c in message.upper():
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def get_decryption_key(key):
    d_key = {}
    for c in key:
        d_key[key[c]] = c
    return d_key


def break_cipher(cipher, keyspace=KEYSPACE):
    for i in range(len(keyspace)):
        g_key = generate_key(i)
        msg = encrypt_message(g_key, cipher)
        words = [word for word in msg.split(" ") if d.check(word)]
        if len(words) > 3:
            print(msg)


key = generate_key(3)
print(''.join(key.values()))

message = "Hey there, I hope you're having a great day!"
cipher = encrypt_message(key, message)
print(cipher)

d_key = get_decryption_key(key)
d_message = encrypt_message(d_key, cipher)
print(d_message)
print()
print("Now we try to break the cipher!")
break_cipher(cipher)
