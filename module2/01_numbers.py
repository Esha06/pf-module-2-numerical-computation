# Module 2 - Part 2: Numerical computation
a = 17
b = 5

print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)      # true division: always a float
print("a // b =", a // b)     # floor division
print("a % b  =", a % b)      # remainder
print("a ** b =", a ** b)     # power
print("divmod(a, b) =", divmod(a, b))

print()
print("-7 // 2 =", -7 // 2)           # floors towards minus infinity
print("-2 ** 2 =", -2 ** 2)           # ** is done before the minus sign
print("(-2) ** 2 =", (-2) ** 2)
print("2 ** 100 =", 2 ** 100)         # int has no size limit
print("1e308 * 10 =", 1e308 * 10)     # float does
print("type(3) =", type(3), " type(3.0) =", type(3.0))
print("int(7.9) =", int(7.9))
print("round(7.5) =", round(7.5), " round(8.5) =", round(8.5))
