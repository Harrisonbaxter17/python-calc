def calculate():
    def welcoming():
        print("""
        welcome to the python calculator""")

    welcoming()

    operation = input("""
    please type the operator you wold like to perform
    + for addition
    - for subtraction
    * for multiplication
    / for division
    """)

    number_1 = int(input("enter the first number"))
    number_2 = int(input("enter the second number"))

    if operation == "+":
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == "-":
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == "*":
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == "/":
        print("{} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print("you have entered an incorrect operator, try agian")

    again()


def again():
    calculator_again = input(("""
    do you want to use the calculator again?
    please type Y for YES or N for NO
    """))
    if calculator_again == "Y":
        calculate()
    elif calculator_again == "N":
        print("goodbye!")
    else:
        again()


calculate()

calculate()
