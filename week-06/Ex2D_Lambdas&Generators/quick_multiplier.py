doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# ============================== #

tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# =============================== #

def multiplier(x):
    return lambda n: n * x

t4 = multiplier(4)
t5 = multiplier(5)
t6 = multiplier(6)
t7 = multiplier(7)
t8 = multiplier(8)
t9 = multiplier(9)
t10 = multiplier(10)

print(t4(5))
print(t5(5))
print(t6(5))
print(t7(5))
print(t8(5))
print(t9(5))
print(t10(5))


