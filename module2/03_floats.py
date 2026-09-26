# Module 2 - Part 4: Floating-point precision
import math
from decimal import Decimal
from fractions import Fraction

print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)
print(f"0.1 is stored as {0.1:.20f}")
print("math.isclose(0.1 + 0.2, 0.3) ->", math.isclose(0.1 + 0.2, 0.3))

total = 0.0
for _ in range(10):
    total += 0.1
print("0.1 added ten times =", total)
print("math.fsum of ten 0.1 =", math.fsum([0.1] * 10))

print("round(2.675, 2) =", round(2.675, 2))
print(f"2.675 is stored as {2.675:.20f}")
print("(1e16 + 1) - 1e16 =", (1e16 + 1) - 1e16)

print("Decimal:", Decimal("0.1") + Decimal("0.2"))
print("Fraction:", Fraction(1, 10) + Fraction(2, 10))
