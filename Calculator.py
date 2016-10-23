from math import sqrt

prompt = """
Welcome to the calculator!
         Operation : Command
         -------------------
          Addition : add
       Subtraction : subtract
    Multiplication : multiply
          Division : divide
          Squaring : square
       Square-root : root

           To quit : quit
"""


separator = "=" * 35


def get_two_numbers():
  number1 = float(input("\t Enter the first number > "))
  number2 = float(input("\tEnter the second number > "))
  return number1, number2


def get_one_number():
  return float(input("Enter a number > "))


def add():
    number1, number2 = get_two_numbers()
    print('The answer is {}'.format(number1 + number2))
    print(separator)


def subtract():
    print("Remember order matters for subtraction! ")
    number1, number2 = get_two_numbers()
    print('The answer is {}'.format(number1 - number2))
    print(separator)


def multiply():
    number1, number2 = get_two_numbers()
    print('The answer is {}'.format(number1 * number2))
    print(separator)


def divide():
    print("Remember order matters for division! ")
    number1, number2 = get_two_numbers()
    print('The answer is {}'.format(number1 / number2))
    print(separator)


def square():
    number = get_one_number()
    print('The answer is {}'.format(number * number))
    print(separator)


def root():
    number = get_one_number()
    print('The answer is {}'.format(sqrt(number)))
    print(separator)


options = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'square': square,
    'root': root
}


while True:
    print(prompt)
    option = input("Please enter an option: ")
    if option == "quit":
        break
    try:
        options[option]()
    except KeyError:
        print('Invalid operation.')
