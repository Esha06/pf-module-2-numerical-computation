# Module 2 - Part 7: Nested lists and dictionaries
import json

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("row 1:", matrix[1])
print("row 1, column 2:", matrix[1][2])
print("first column:", [row[0] for row in matrix])
print("transpose:", [list(col) for col in zip(*matrix)])

experiments = {
    "EXP-01": {"material": "steel", "temps_C": [20, 150, 300], "passed": True},
    "EXP-02": {"material": "aluminium", "temps_C": [20, 90], "passed": False},
}
print(experiments["EXP-01"]["material"])
print(experiments["EXP-01"]["temps_C"][-1])

experiments["EXP-02"]["temps_C"].append(120)
experiments["EXP-03"] = {"material": "copper", "temps_C": [20, 60], "passed": True}

for exp_id, info in experiments.items():
    print(f"{exp_id}: {info['material']:<10} max {max(info['temps_C']):>3} C  passed={info['passed']}")

print(json.dumps(experiments["EXP-03"], indent=2))

grid = [[0] * 3] * 3            # trap: the same inner list three times
grid[0][0] = 1
print("trap:   ", grid)
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 1
print("correct:", grid)
