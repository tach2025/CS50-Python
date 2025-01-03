# Prompt user for a camelCase name
camel = input("camelCase: ").strip()
print("snake_case:", end='')
for i in camel:
    if i.isupper():
        print(f"_{i.lower()}", end='')
    else:
        print(i, end='')
