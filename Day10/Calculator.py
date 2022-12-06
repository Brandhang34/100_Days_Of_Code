import art

print(art.logo)

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def calculation(a):
    operation_symbol = input("Pick another operation: ")
    b = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    return(calculation_function(a, b))

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    }

def calculator():
    num1 = float(input("what is the first number? "))

    for i in operations:
        print(i)
    operation_symbol = input("Pick an operation from the line above: ")
    calculation_function = operations[operation_symbol]
    num2 = float(input("what is the second number? "))
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")


    cont = True
    while cont:
        inp = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ")
        if inp == 'y':
            print(calculation(first_answer))
        else:
            cont = False
            calculator()

calculator()