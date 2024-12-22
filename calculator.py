from art import logo

def add(n1, n2):
    return n1 + n2
# TODO: Write out the other 3 function - subtract, multiply, divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
  
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
}

def calculator():
    replay = True
    print(logo)
    number1 = float(input("What's the first number: "))

    while replay:
        number2 = float(input("What's the next number: "))
        for operation in operations:
            print(operation)
        operation = input("Pick an operation: ")
        result = operations[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {result}")

        continue_with_previous_result = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")

        if continue_with_previous_result == "y":
            number1 = result
        else:
            replay = False
            print("\n" * 20)
            calculator()

calculator()
