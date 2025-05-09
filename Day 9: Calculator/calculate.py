# code 

from IPython.utils.coloransi import value


def add(n1, n2):
    return n1 + n2
# TODO :  Write the other 3 functions
def sub(n1,n2):
    return n1 - n2
def multi(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1/n2

operation = {
            "+": add,
            "-": sub,
            "*": multi,
            "/": div
        }
def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number? :"))

    while should_accumulate:

        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation")
        num2 = float(input("What is the next number?"))
        answer = operation[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type y to continue calculation with {answer}, or  type n to start new calculation")

        if choice == "y":
            num1 = answer
        else :
            should_accumulate = False
            print("\n" * 20)
            calculator() # function inside a function is called recursion 





# TODO : Add these 4 functions into a dictionary as the vales
# Todo: use the dictionary operation to perform the calculation
#  multiply 4 * 8 using the dictionary
"""game = 0
game_over = False
while game_over == False:
    def number():
        operation = {
            "+": add,
            "-": sub,
            "*": multi,
            "/": div
        }
        value_input = int(input("What is the first number?"))
        operation_value = input("Pick an operation from above?")
        value2_input = int(input("What is the Second number?"))


        if operation_value == "+":
            game = operation["+"](value_input, value2_input)
            print(f"{value_input}{operation_value}{value2_input} = {game}")
        elif operation_value == "-":
            game = operation["-"](value_input, value2_input)
            print(f"{value_input}{operation_value}{value2_input} = {game}")
        elif operation_value == "*":
            game =  operation["*"](value_input, value2_input)
            print(f"{value_input}{operation_value}{value2_input} = {game}")
        elif operation_value == "/":
            game = operation["/"](value_input, value2_input)
            print(f"{value_input}{operation_value}{value2_input} = {game}")
        else:
            print("Please give valid input")

    number()

    replay = input("Do you want to play again Yes or No").lower()
    if replay == "yes":
        game_over = True
        value_input = game
        number()
    else:
        game_over = False

"""
