import sys

from src.math import Math


def start_math(number1: float, number2: float):
    print(f"Executing math methods on {number1} and {number2} numbers:")

    result = Math.plus(x=number1,
                       y=number2)

    print(f"{number1} + {number2} is {result}")

    result = Math.minus(x=number1,
                        y=number2)

    print(f"{number1} - {number2} is {result}")

    result = Math.multiplication(x=number1,
                                 y=number2)

    print(f"{number1} * {number2} is {result}")

    result = Math.divide(x=number1,
                         y=number2)

    print(f"{number1} : {number2} is {result}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = float(sys.argv[1])
    y = float(sys.argv[2])

    start_math(number1=x,
               number2=y)
