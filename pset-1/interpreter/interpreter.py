# Prompt the user for an arithmetic expression
exp = input("Expression: ")
# Split the exp to get operand and operator
x, y, z = exp.split()
# Convert the operands to float
x = float(x)
z = float(z)

# Perform operations according to operator
match y:
    case '+':
        print(x + z)
    case '-':
        print(x - z)
    case '*':
        print(x * z)
    case '/':
        print(x / z)
