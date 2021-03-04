# python has the walrus operator and list comprehensions so it will always win!
print(y := [x for x in range(11) if x % 2 == 0])
print(sorted(y + [x for x in range(10) if x % 2 != 0]))
print(S := [2 * x for x in range(100) if x ** 2 > 500])