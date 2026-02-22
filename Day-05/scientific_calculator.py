# USER INPUT BASED SCIENTIFIC CALCULATOR
# Supports: +, -, *, /, power, factorial, square root, cube root, derivatives & integration

import math
import sympy as sp

# Symbol for calculus
x = sp.symbols('x')

# FUNCTIONS
def addition():
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("Result:",a+b)

def subtraction():
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("Result:",a-b)

def multiplication():
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("Result:",a*b)

def division():
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    if b==0:
        print("Division by zero error")
    else:
        print("Result:",a/b)

def power():
    a=float(input("Enter base: "))
    b=float(input("Enter power: "))
    print("Result:",a**b)

def factorial():
    n=int(input("Enter integer: "))
    print("Result:",math.factorial(n))

def square_root():
    n=float(input("Enter number: "))
    print("Result:",math.sqrt(n))

def cube_root():
    n=float(input("Enter number: "))
    print("Result:",n**(1/3))

def derivative():
    expr=input("Enter function in x (example: x**2 + 3*x): ")
    f=sp.sympify(expr)
    print("Derivative:",sp.diff(f,x))

def integration():
    expr=input("Enter function in x (example: x**2 + 3*x): ")
    f=sp.sympify(expr)
    print("Integration:",sp.integrate(f,x))


# ============================================================
# MAIN MENU
# ============================================================

while True:

    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("1  -> Addition")
    print("2  -> Subtraction")
    print("3  -> Multiplication")
    print("4  -> Division")
    print("5  -> Power")
    print("6  -> Factorial")
    print("7  -> Square Root")
    print("8  -> Cube Root")
    print("9  -> Derivative")
    print("10 -> Integration")
    print("0  -> Exit")

    choice=input("Enter choice: ")

    if choice=='1':
        addition()
    elif choice=='2':
        subtraction()
    elif choice=='3':
        multiplication()
    elif choice=='4':
        division()
    elif choice=='5':
        power()
    elif choice=='6':
        factorial()
    elif choice=='7':
        square_root()
    elif choice=='8':
        cube_root()
    elif choice=='9':
        derivative()
    elif choice=='10':
        integration()
    elif choice=='0':
        print("Calculator Closed")
        break
    else:
        print("Invalid Choice")
