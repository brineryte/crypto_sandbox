from itertools import permutations
import cProfile

# Permutations
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

perm = [p for p in permutations(my_list)]
print(f"{len(my_list)} {len(perm)}")


# Factorial!
def factorial(n):
    return 1 if n == 1 else factorial(n - 1) * n


print(factorial(9))


# Counter
def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt


cProfile.run("counter(factorial(11))")
