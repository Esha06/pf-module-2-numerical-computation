# Module 2 - Part 5: String manipulation and formatting
raw = "   T-101 , reactor TEMPERATURE ,  351.2749 , kelvin  "

parts = [p.strip() for p in raw.split(",")]
print(parts)

tag, name, value, unit = parts
name = name.title()
value = float(value)
print(tag, "|", name, "|", value, "|", unit.upper())

print(name.lower())
print(name.replace("Reactor", "Boiler"))
print("find('Temp') ->", name.find("Temp"))
print("startswith('Reactor') ->", name.startswith("Reactor"))
print("first char:", tag[0], " last 3:", tag[-3:], " reversed:", name[::-1])
print(" | ".join(parts))

print()
print(f"{name}: {value:.2f} K")
print(f"[{tag:<10}] [{tag:>10}] [{tag:^10}]")
print(f"{1234567.891:,.2f}")
print(f"{0.000123:.2e}")
print(f"{0.4567:.1%}")
print(f"{42:05d}")
print(f"{value=}")
