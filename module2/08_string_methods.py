# Module 2 - Part 9: Python string methods reference
methods = [m for m in dir(str) if not m.startswith("_")]
print(len(methods), "string methods")
print(methods[:12])

print("'  hi  '.strip() ->", repr("  hi  ".strip()))
print("'flow rate'.title() ->", "flow rate".title())
print("'a,b,c'.split(',') ->", "a,b,c".split(","))
print("'-'.join(['a', 'b']) ->", "-".join(["a", "b"]))
print("'1,5'.replace(',', '.') ->", "1,5".replace(",", "."))
print("'data.csv'.endswith('.csv') ->", "data.csv".endswith(".csv"))
print("'42'.isdigit() ->", "42".isdigit())
print("'7'.zfill(3) ->", "7".zfill(3))
print("'ok'.center(6, '*') ->", "ok".center(6, "*"))
print("'banana'.count('a') ->", "banana".count("a"))
