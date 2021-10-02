from factorial import factorial
from exp_root import exponentiation, root
from logarithm import logarithm

def input_int(message, c):
    while True:
        try:
            num = int(input(message))
            if c:
                if num <= 1:
                    raise ValueError("Only positive integers")
            if num < 0:
                raise ValueError("Only positive integers")
            if not int(num):
                raise ValueError("Only integers")
            return num
        except ValueError as ve:
            print(ve)
            continue
def input_float(message, c):
    while True:
        try:
            num = float(input(message))
            if c:
                if num < 0:
                    raise ValueError("Only positive floating numbers")
            if not float(num):
                raise ValueError("Only floating numbers")
            return num
        except ValueError as ve:
            print(ve)
            continue

def main():
    print("\nWhat function you would like to use?")
    print("1. Find factorial of number")
    print("2. Find square the number")
    print("3. Find cube the number")
    print("4. Find the root of the number")
    print("5. Find the root of a third degree number")
    print("6. Find logarithm of two numbers")
    print("7. Find natural logarithm of number")
    print("8. Find decimal logarithm of numbers")
    answer = input("Input number: ")
    if answer == "1":
        num = input_int("\nYour number: ", False)
        print("Factorial of", num, "=", factorial.factorial(num))
    elif answer == "2":
        num = input_float("\nYour number: ", False)
        print("Square of", num, "=", exponentiation.exp2(num))
    elif answer == "3":
        num = input_float("\nYour number: ", False)
        print("Cube of", num, "=", exponentiation.exp3(num))
    elif answer == "4":
        num = input_float("\nYour number: ", True)
        print("The root of", num, "=", root.root2(num))
    elif answer == "5":
        num = input_float("\nYour number: ", True)
        print("The third degree root of", num, "=", root.root3(num))
    elif answer == "6":
        a = input_int("\nYour a: ", True)
        b = input_int("Your b: ", False)
        print("Logarithm of", a,",",b, "=", logarithm.log(a, b))
    elif answer == "7":
        num = input_int("\nYour number: ", False)
        print("Natural logarithm of", num, "=", logarithm.ln(num))
    elif answer == "8":
        num = input_int("\nYour number: ", False)
        print("Decimal logarithm of", num, "=", logarithm.lg(num))
    else:
        print("There is no option with such a number")

if __name__ == '__main__':
    main()

