import random


# LCG linear congruential generator (look up on wiki)
class KeyStream:
    def __init__(self, key=1):
        self.next = key

    # PSG
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


def modification(cipher):
    mod = [0] * len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])


def crack(key_stream, cipher):
    length = min(len(key_stream), len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(length)])

def run_txmt_example():
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
    print(encrypt(key, cipher))
    print()


def run_alice_bob_money_example():
    # ----------- new scenario --------------
    # this is alice
    key = KeyStream(10)
    message = "Send Bob:   10$".encode()
    print(message)
    cipher = encrypt(key, message)
    print(cipher)

    # this is bob
    cipher = modification(cipher)

    # this is bank
    key = KeyStream(10)
    message = encrypt(key, cipher)
    print(message)


# ------------- new scenario 2 -----------
def run_alice_eve_example():
    # Eve goes to Alice
    eves_message = "This is Eve's most valued secrets of all her life".encode()

    # This is Alice alone
    key = KeyStream(10)
    message = eves_message
    print(message)
    cipher = encrypt(key, message)
    print(cipher)

    # This is Eve alone (evil)
    eves_key_stream = get_key(message, cipher)

    # This is Bob
    key = KeyStream(10)
    message = encrypt(key, cipher)
    print(message)

    print()

    # Alice again
    print(message := "Hi Bob, let's meet and plan our world domination".encode())
    key = KeyStream(10)
    print(cipher := encrypt(key, message))

    # Bob again
    key = KeyStream(10)
    print(message := encrypt(key, cipher))

    # Eve again
    print("THIS IS EVE")
    print(crack(eves_key_stream, cipher))

run_alice_eve_example()
