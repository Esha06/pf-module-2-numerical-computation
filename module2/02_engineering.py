# Module 2 - Part 3: Engineering formula evaluation

# Ohm's law (V = I * R) and electrical power (P = V * I)
voltage = 230.0        # V
resistance = 52.9      # ohm
current = voltage / resistance      # A
power = voltage * current           # W
print(f"Current = {current:.3f} A, Power = {power:.1f} W")

# Reynolds number: Re = density * velocity * diameter / viscosity
density = 998.0        # kg/m^3 (water at 20 C)
velocity = 1.5         # m/s
diameter = 0.05        # m
viscosity = 1.002e-3   # Pa*s
reynolds = density * velocity * diameter / viscosity
if reynolds < 2300:
    regime = "laminar"
elif reynolds > 4000:
    regime = "turbulent"
else:
    regime = "transitional"
print(f"Re = {reynolds:,.0f} -> {regime} flow")

# Bending stress in a rectangular beam: stress = M * y / I, with I = b * h^3 / 12
width = 0.10           # m
height = 0.20          # m
moment = 15_000        # N*m
second_moment = width * height ** 3 / 12     # m^4
y_max = height / 2                           # m
stress = moment * y_max / second_moment      # Pa
print(f"I = {second_moment:.3e} m^4, max stress = {stress / 1e6:.2f} MPa")
