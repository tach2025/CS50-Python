grocery = {}

while True:
    try:
        item = input().upper()
        grocery[item] += 1
    except EOFError:
        break
    except KeyError:
        grocery[item] = 1

for k in sorted(grocery):
    print(f"{grocery[k]} {k}")
