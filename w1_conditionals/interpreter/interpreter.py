expression = input("Expression: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

match y:
    case '+':
        print(x + z)
    case '-':
        print(x - z)
    case '*':
        print(x * z)
    case '/':
        print(x / z)

# # using the built-in function eval()
# result = float(eval(expression))

# print(f"{result}")
