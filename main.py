import time
import math
import sys
def calc():
    print("------------------------------------------------------")
    print("-----------WELCOME TO THE PYTHON CALCULATOR-----------")
    print("------------------------------------------------------")

    operator = input("""please chose an operator:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        <> for square root of (x)
        : """)
        
    number1 = input("enter the first number: ")

    print()

    number2 = input("enter the second number: ")
    

    def addition():
        total = float(number1) + float(number2)
        print(f"{number1} + {number2} = {total}")

    def subtraction():
        total = float(number1) - float(number2)
        print(f"{number1} - {number2} = {total}")

    def multiplication():
        total = float(number1) * float(number2)
        print(f"{number1} * {number2} = {total}")

    def division():
        total = float(number1) / float(number2)
        print(f"{number1} / {number2} = {total}")


    if operator == "+":
        addition()
    elif operator == "-":
        subtraction()
    elif operator == "*":
        multiplication()
    elif operator == "/":
        division()
    else:
        print("you have typed an incorrect operator")

    again()


def again():
    calculator_again = input("""
    do you want to use the calculator again?
    please type Y for YES or N for NO
    """).upper()

    if calculator_again == "Y":
        calc()
    elif calculator_again == "N":
        print("THANK-YOU FOR USING THE PYTHON CALCULATOR, GOODBYE")
        print("EXITING.")
        time.sleep(0.5)
        print("EXITING..")
        time.sleep(0.5)
        print("EXITING...")
        time.sleep(0.5)
        print("EXITING....")
        time.sleep(0.5)
        print("EXITING.....")
        sys.exit(0)
        

calc()



