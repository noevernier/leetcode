from random import randint

tot = 0
n = 10000000
for _ in range(n):
    a = [randint(1, 6) for _ in range(5)]
    a.sort()
    if sum(a[-4:-1]) == 18:
        tot += 1

print(tot/n)