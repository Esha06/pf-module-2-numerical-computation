# Module 2 - Part 6: Collection operations
readings = [23.1, 22.8, 24.5, 23.9]
readings.append(25.2)
readings.extend([21.7, 22.0])
print("readings:", readings)
print("count:", len(readings), " first:", readings[0], " last:", readings[-1])
print("slice [1:4]:", readings[1:4])
print("sorted:", sorted(readings))
print("min:", min(readings), " max:", max(readings))
print("mean:", round(sum(readings) / len(readings), 2))
print("above 23:", [r for r in readings if r > 23])

point = (3.0, 4.0)
x, y = point
print("tuple unpacked: x =", x, " y =", y)

group_a = {"S1", "S2", "S3"}
group_b = {"S3", "S4"}
print("union:", sorted(group_a | group_b))
print("intersection:", sorted(group_a & group_b))
print("difference:", sorted(group_a - group_b))

constants = {"g": 9.81, "c": 299_792_458}
constants["h"] = 6.626e-34
print("g =", constants["g"])
print("k =", constants.get("k", "not defined"))
for key, val in constants.items():
    print(" ", key, "=", val)

quantities = ["mass", "speed", "time"]
values = [2.0, 3.5, 10]
print(dict(zip(quantities, values)))
for i, q in enumerate(quantities, start=1):
    print(i, q)
