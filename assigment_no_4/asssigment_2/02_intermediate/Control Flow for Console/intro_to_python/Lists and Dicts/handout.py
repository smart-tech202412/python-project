def access_element(lst, index):
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Index out of range."


def modify_element(lst, index, new_value):
    try:
        old_value = lst[index]
        lst[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}' at index {index}."
    except IndexError:
        return "Index out of range."


def slice_list(lst, start, end):
    try:
        return f"Sliced list [{start}:{end}]: {lst[start:end]}"
    except Exception as e:
        return f"Error slicing list: {e}"


def index_game():
    # Sample initial list
    data_list = ['red', 'blue', 'green', 'yellow', 'purple']
    print("Initial List:", data_list)

    while True:
        print("\nChoose an operation:")
        print("1 - Access an element")
        print("2 - Modify an element")
        print("3 - Slice the list")
        print("4 - Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print(access_element(data_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(data_list, index, new_value))
            print("Updated List:", data_list)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(data_list, start, end))

        elif choice == '4':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main():
    print("== Problem #1: List Practice ==")
    

    print("\n== Problem #2: Index Game ==")
    index_game()


if __name__ == '__main__':
    main()
