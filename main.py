import time 
import math
import sys

def calc():

    choice = input("""please chose which number you would like to perform:

-------------------------
--------Number 1---------
-------------------------

+ for addition 
- for subtraction
* for multiplication
/ for division
_________________________


-------------------------
--------Number 2---------
-------------------------

<> for square root of (x)
_________________________

: """)


    if choice == "1":
        Basic_Math()
    elif choice == "2":
        Advanced_math()
    else:
        print("you typed an incorrect operator, please wait to restart!")
        time.sleep(3)
        calc()
    
def Basic_Math():

    operation = input("""please chose an operator:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    : """)

    number1 = input("please enter the first number: ")
    print()
    number2 = input("please enter the second number: ")

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

    if operation == "+":
        addition()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiplication()
    elif operation == "/":
        division()
    else:
        print("you have typed an incorrect operator")

    again()

def again():
    calculator_again = input("""
do you want to use the calculator again?
type Y for YES or N for NO
""").upper()

    if calculator_again == "Y":
        calc()
    elif calculator_again == "N":
        print("THANK-YOU FOR USING THE PYTHON CALCULATOR, GOODBYE!")
        print("EXITING.")
        time.sleep(0.5)
        print("EXITING..")
        time.sleep(0.5)
        print("EXITING...")
        time.sleep(0.5)
        print("EXITING....")
        time.sleep(0.5)
        print("EXITING.....")
        time.sleep(0.5)
        print("EXITING....")
        time.sleep(0.5)
        print("EXITING...")
        sys.exit(0)



def Advanced_math():

    operation = input("""please chose an operator:
    <> for the square root of (n)
    : """)
        
    number1 = input("please enter a number to perfrom the square root on: ")

    def sqrt():
        total = math.sqrt(float(number1))
        print(str(total))
        
    if operation == "<>":
        sqrt()
    again()

def again():
    calculator_again = input("""
do you want to use the calculator again?
type Y for YES or N for NO
""").upper()

    if calculator_again == "Y":
        calc()
    elif calculator_again == "N":
        print("THANK-YOU FOR USING THE PYTHON CALCULATOR, GOODBYE!")
        print("EXITING.")
        time.sleep(0.5)
        print("EXITING..")
        time.sleep(0.5)
        print("EXITING...")
        time.sleep(0.5)
        print("EXITING....")
        time.sleep(0.5)
        print("EXITING.....")
        time.sleep(0.5)
        print("EXITING....")
        time.sleep(0.5)
        print("EXITING...")
        sys.exit(0)


calc()
