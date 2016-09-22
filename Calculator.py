from math import sqrt

while True:
    print("Welcome to the calculator!")
    print("For addition enter add")
    print("For subtraction enter subtract")
    print("For multiplication enter multiply")
    print("For division enter divide")
    print("For squaring enter square")
    print("For square-root enter root")
    print("To quit enter quit")
    option = input("Please enter an option: ")

    if option == "quit":
          break
    elif option == "add":
          number1 = float(input("Enter the first number. "))
          number2 = float(input("Enter the second number. "))
          answer = str(number1 + number2)
          print("The answer is " + answer)
          print("=" * 35)
    elif option == "subtract":
          print("Remember order matters for subtraction! ")
          number1 = float(input("Enter the first number. "))
          number2 = float(input("Enter the second number. "))
          answer = str(number1 - number2)
          print("The answer is " + answer)
          print("=" * 35)
    elif option == "multiply":
          number1 = float(input("Enter the first number. "))
          number2 = float(input("Enter the second number. "))
          answer = str(number1 * number2)
          print("The answer is " + answer)
          print("=" * 35)
    elif option == "divide":
          print("Remember order matters for division! ")
          number1 = float(input("Enter the first number (dividend) "))
          number2 = float(input("Enter the second number (divisor) "))
          answer = str(number1 / number2)
          print("The answer is " + answer)
          print("=" * 35)
    elif option == "square":
          number1 = float(input("Enter a number. "))
          answer = str(number1 * number1)
          print("The answer is " + answer)
          print("=" * 35)
    elif option == "root":
          number1 = float(input("Enter a number. "))
          answer = str(sqrt(number1))
          print("The answer is " + answer)
          print("=" * 35)
    else:
          print("Unknown option!")
          print("=" * 35)
