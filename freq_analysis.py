import operator
import sys

cipher_text = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""


class Attack1:
    """
    This attack looks at every letter in the english language
    """

    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.plain_chars_left = "" + self.alphabet
        self.cipher_chars_left = "" + self.alphabet
        self.key = {}
        self.freq = {}
        self.freq_eng = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
                         'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
                         'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
                         's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
                         'y': 0.0197, 'z': 0.0007}
        self.mappings = {}

    def calculate_freq(self, cipher):
        clean_cipher = cipher.replace(' ', '').replace('\n', '')
        for letter in self.alphabet:
            self.freq[letter] = round(clean_cipher.count(letter) / len(clean_cipher), 4)

    def print_freq(self):
        for c in self.freq:
            print(c + " : " + str(self.freq[c]))

    def get_freq(self):
        return self.freq

    def calculate_matches(self):
        for cipher_char in self.alphabet:
            map = {}
            for plain_char in self.alphabet:
                map[plain_char] = round(abs(self.freq[cipher_char] - self.freq_eng[plain_char]), 4)
            self.mappings[cipher_char] = sorted(map.items(), key=operator.itemgetter(1))

    def set_key_mapping(self, cipher_char, plain_char):
        if cipher_char not in self.cipher_chars_left and plain_char not in self.plain_chars_left:
            print("ERROR: key mapping error", cipher_char, plain_char)
            sys.exit(-1)
        self.key[cipher_char] = plain_char
        self.plain_chars_left = self.plain_chars_left.replace(plain_char, '')
        self.cipher_chars_left = self.cipher_chars_left.replace(cipher_char, '')

    def guess_key(self):
        for cipher_char in self.cipher_chars_left:
            for plain_char, diff in self.mappings[cipher_char]:
                if plain_char in self.plain_chars_left:
                    self.key[cipher_char] = plain_char
                    self.plain_chars_left = self.plain_chars_left.replace(plain_char, '')
                    break

    def get_key(self):
        return self.key


class Attack2:
    """
    This attack only considers chars that are IN the cipher
    """

    def __init__(self):
        self.freq = {}

    def calculate_freq(self, cipher):
        clean_cipher = cipher.replace(' ', '').replace('\n', '')
        distinct = set(clean_cipher)

        for letter in distinct:
            self.freq[letter] = round(clean_cipher.count(letter) / len(clean_cipher), 4)

    def print_freq(self):
        for index, key in enumerate(sorted(self.freq)):
            print(key + ": " + str(self.freq[key]) + "  ", end="")
            if (index + 1) % 4 == 0:
                print()

    def get_freq(self):
        return self.freq


def decrypt(key, cipher):
    message = ""
    for c in cipher:
        if c in key:
            message += key[c]
        else:
            message += c
    return message


attack = Attack1()
attack.calculate_freq(cipher_text)
attack.print_freq()
attack.calculate_matches()
print()
for c in attack.mappings:
    print(c, attack.mappings[c])

print()

attack.set_key_mapping('r', 'e')
attack.set_key_mapping('v', 'c')
attack.set_key_mapping('m', 'a')
attack.set_key_mapping('p', 'h')
attack.set_key_mapping('w', 'i')
attack.set_key_mapping('s', 'p')
attack.set_key_mapping('u', 'r')
attack.set_key_mapping('x', 'f')
attack.set_key_mapping('e', 'v')
attack.set_key_mapping('q', 'k')
attack.set_key_mapping('t', 'y')
attack.set_key_mapping('d', 'd')
attack.set_key_mapping('c', 'w')
attack.set_key_mapping('a', 'x')
attack.set_key_mapping('f', 'q')

attack.guess_key()
print(key := attack.get_key())

message_guess = decrypt(key, cipher_text)

for index, line in enumerate(cipher_text.splitlines()):
    print("P: ", message_guess.splitlines()[index])
    print("C: ", line)
