def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
# print(operations["*"](4,8))
from art import logo

def calculator():
    print(logo)
    should_accumulate = True
    first_number= float(input("whats the first number?: "))
    while should_accumulate:
        for key in operations:
            print(key)
        operator=input("Pick an operation: ")

        second_number=float(input("What is the next number?: "))
        result = operations[operator](first_number,second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        choice =input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            first_number= result

        else:
            should_accumulate = False
            print("\n"*20)
            calculator()
calculator()






