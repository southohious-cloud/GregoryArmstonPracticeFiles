expression = input("Expression: ")

x, y, z = expression.split()

n1 = float(x)
n2 = float(z)

if y == "+":
    result = n1 + n2
elif y == "-":
    result = n1 - n2
elif y == "*":
    result = n1 * n2
elif y == "/":
    result = n1 / n2
else:
    raise ValueError("Invalid operator")

print(f"{result:.1f}")
