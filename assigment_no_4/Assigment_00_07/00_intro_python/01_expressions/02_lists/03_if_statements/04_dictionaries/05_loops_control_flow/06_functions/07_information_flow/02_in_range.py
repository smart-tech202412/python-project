def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    return low <= n <= high

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the low end of the range: "))
    high = int(input("Enter the high end of the range: "))
    
    if in_range(n, low, high):
        print(f"{n} is in the range [{low}, {high}].")
    else:
        print(f"{n} is NOT in the range [{low}, {high}].")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
