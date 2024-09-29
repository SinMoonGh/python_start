import art


def add(n1, n2):
  return n1 + n2


def Subtract(n1, n2):
  return n1 - n2


def Multiply(n1, n2):
  return n1 * n2


def Divide(n1, n2):
  return n1 / n2


operator_dictionary = {'+': add, '-': Subtract, '*': Multiply, '/': Divide}


def restart():
  print(art.logo)
  num1 = float(input("What's the first number? : "))

  for symbol in operator_dictionary:
    print(symbol)

  operation_symbol = input('Pick an operation from the line above: ')

  num2 = float(input("What's the next number? : "))

  calculator = operator_dictionary[operation_symbol]
  first_answer = calculator(num1, num2)

  print(f'{num1} {operation_symbol} {num2} = {first_answer}')

  while True:
    choice = input(
        f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit and restart 'r' : "
    )

    if choice == 'n':
      break
    elif choice == 'r':
      return restart()

    for symbol in operator_dictionary:
      print(symbol)

    operation_symbol = input('Pick another operation: ')
    num3 = float(input("What's the next number? : "))
    calculator = operator_dictionary[operation_symbol]
    second_answer = calculator(first_answer, num3)
    print(f'{first_answer} {operation_symbol} {num3} = {second_answer}')
    first_answer = second_answer


restart()
