def print_ones_digit(num):
    ones_digit = num % 10
    print("The ones digit is", ones_digit)

def main():
    number = int(input("Enter a number: "))
    print_ones_digit(number)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
