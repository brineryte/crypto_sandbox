import random


# LCG linear congruential generator (look up on wiki)
class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2 ** 31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2 ** random.randrange(0, 8)
        b.append(c)
    return bytes(b)


# flip 6th bit of 4th byte (for quiz)
def transmit_alt(cipher):
    b = []
    for idx, c in enumerate(cipher):
        if idx == 3:
            b.append(c ^ 2 ** 5)
        else:
            b.append(c)
    return b


key = KeyStream(1929)

# print rand output
# for i in range(10):
#     print(key.get_key_byte())

message = "Can you understand this? Reply yes or no.".encode()
print(cipher := encrypt(key, message))

# reset the key (pretty important ;) )
key = KeyStream(1929)
print(decrypted := encrypt(key, cipher))

key = KeyStream(10)
cipher = encrypt(key, message)

cipher = transmit(cipher, 5)

key = KeyStream(10)
print(message := encrypt(key, cipher))
