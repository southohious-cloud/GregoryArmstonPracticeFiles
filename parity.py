def main():
    x = get_int("What's X? ")
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def is_even(n):
    return n % 2 == 0


main()
