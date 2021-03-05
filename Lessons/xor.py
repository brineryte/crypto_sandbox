def xor(x, s):
    print(x, " xor ", s, " = ", x ^ s)


def bin_xor(x, s):
    print(bin(x), " xor ", bin(s), " = ", bin(x ^ s))


xor(4, 8)
xor(1, 1)
xor(3, 4)
xor(4, 3)
xor(3, 7)
xor(4, 7)
xor(255, 128)

bin_xor(255, 128)
bin_xor(4, 4)
bin_xor(255, 1)
