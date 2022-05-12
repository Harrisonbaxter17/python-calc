import sys
import time
import math


def calc():
    def welcome():
        print()
        print("--------------------------------")
        print("WELCOME TO THE PYTHON CALCULATOR")
        print("--------------------------------")
        print()

    welcome()

    choice = input("""please choose a number to perform:
    1. addition 
    2. subtraction
    3. multiplication 
    4. division
    5. √ (square root)
    6. x²
    7. a²+b² = c² (Pythagorean Theorem)
    8.
    : """)

    def add():
        number1 = input("please enter the first number: ")
        number2 = input("please enter the first number: ")
        total = float(number1) + float(number2)
        print(f"{number1} + {number2} = {total}")

    def sub():
        number1 = input("please enter the first number: ")
        number2 = input("please enter the first number: ")
        total = float(number1) - float(number2)
        print(f"{number1} - {number2} = {total}")

    def mult():
        number1 = input("please enter the first number: ")
        number2 = input("please enter the first number: ")
        total = float(number1) * float(number2)
        print(f"{number1} * {number2} = {total}")

    def div():
        number1 = input("please enter the first number: ")
        number2 = input("please enter the first number: ")
        total = float(number1) / float(number2)
        print(f"{number1} / {number2} = {total}")

    def root():
        number1 = input("please enter a number to square root: ")
        total = math.sqrt(float(number1))
        print(f"the √ of {number1} =  {total}")

    def square():
        x = float(input("please enter a number to square: "))
        y = float(input("please enter the power number (x²): "))
        total = math.pow(x, y)
        print(f"{x} ** {y} = {total}")

    def a_Pythag():
        c = float(input("enter the length of C: "))
        b = float(input("enter the length of B: "))
        a_squared = c ** 2 - b ** 2
        a = math.sqrt(a_squared)
        print(f"{c}² - {b}² = {a_squared}")
        print(f"√ {a_squared} = {a}")
        print(f"a = {a}")

    def b_Pythag():
        c = float(input("enter the length of C: "))
        a = float(input("enter the length of A: "))
        b_squared = c ** 2 - a ** 2
        b = math.sqrt(b_squared)
        print(f"{c}² - {a}² = {b_squared}")
        print(f"√ {b_squared} = {b}")
        print(f"b = {b}")

    def c_Pythag():
        a = float(input("enter the length of A: "))
        b = float(input("enter the length of B: "))
        c_squared = a ** 2 + b ** 2
        c = math.sqrt(c_squared)
        print(f"{a}² + {b}² = {c_squared}")
        print(f"√ {c_squared} = {c}")
        print(f"c = {c}")

    def pythagorean():
        print("""
                |\          
                | \       
                |  \      
                |   \     
           A    |    \    C
                |     \   
                |      \  
                |       \ 
                ---------        
                
                    B
""")
        selection = input("""please type the letter you want to calculate the value of?
        side A
        side B
        side C
        : """).upper()

        if selection == "A":
            a_Pythag()
        elif selection == "B":
            b_Pythag()
        elif selection == "C":
            c_Pythag()
        else:
            print("you have entered an incorrect option!, please wait")
            time.sleep(2)
            pythagorean()

    if choice == "1":
        add()
    elif choice == "2":
        sub()
    elif choice == "3":
        mult()
    elif choice == "4":
        div()
    elif choice == "5":
        root()
    elif choice == "6":
        square()
    elif choice == "7":
        pythagorean()
    else:
        print("you have entered an incorrect option, please wait to restart!")
        time.sleep(3)
        print("LOADING.")
        time.sleep(0.5)
        print("LOADING..")
        time.sleep(0.5)
        print("LOADING...")
        time.sleep(0.5)
        print("LOADING....")
        time.sleep(0.5)
        calc()

    again()


def again():
    calculator_again = input("""
    do you want to use the calculator again?
    type Y for YES or N for N
    : """).upper()

    if calculator_again == "Y":
        time.sleep(1.5)
        print("LOADING.")
        time.sleep(0.5)
        print("LOADING..")
        time.sleep(0.5)
        print("LOADING...")
        time.sleep(0.5)
        calc()
    elif calculator_again == "N":
        print("THANKYOU FOR USING THE PYTHON CALCULATOR, GOODBYE!")
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
