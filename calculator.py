def add(n1, n2):
    return n1 + n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2
def subtract(n1, n2):
    return n1 - n2

functions = {
    "+": add,
    "/": divide,
    "*": multiply,
    "-": subtract
}

calculating = True
num1 = float(input("What is the first number?:\n"))

while calculating:
    for symbol in functions:
        print(f"{symbol}")
    op_symbol = input("Pick an operation:\n")
    while op_symbol not in functions:
        print("Invalid operation, try again.\n")
        op_symbol = input("Pick an operation:\n")

    num2 = float(input("What is the next number?:\n"))
    answer = functions[op_symbol](num1,num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}\n").lower() != 'y':
        calculating = False
    else:
        num1 = answer