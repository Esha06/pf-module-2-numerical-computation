# Module 2 - Part 8: The math module
import math

print("pi =", math.pi)
print("e =", math.e)
print("sqrt(2) =", math.sqrt(2))
print("hypot(3, 4) =", math.hypot(3, 4))
print("sin(30 deg) =", math.sin(math.radians(30)))
print("45 deg in radians =", math.radians(45))
print("log10(1000) =", math.log10(1000))
print("log(8, 2) =", math.log(8, 2))
print("floor(-2.5) =", math.floor(-2.5), " ceil(-2.5) =", math.ceil(-2.5))
print("factorial(5) =", math.factorial(5))
print("comb(5, 2) =", math.comb(5, 2))
print("gcd(12, 18) =", math.gcd(12, 18))

names = [n for n in dir(math) if not n.startswith("_")]
print(len(names), "names in math, for example:", names[:8])
