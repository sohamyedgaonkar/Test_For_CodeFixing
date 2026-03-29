# simple_broken_script.py

import math
import random   # unused import


# Function with syntax error
def add(a, b)
    return a + b


# Function with NameError
def greet(name):
    print("Hello " + username)


# Function with TypeError
def multiply(a, b):
    return a + "5"


# Function with IndexError
def get_element(lst):
    return lst[10]


# Function with ZeroDivisionError
def divide(a, b):
    return a / b


def main():

    numbers = [1, 2, 3]

    print(add(2, 3))

    greet("Soham")

    print(multiply(5, 3))

    print(get_element(numbers))

    print(divide(10, 0))


if __name__ == "__main__":
    main()
