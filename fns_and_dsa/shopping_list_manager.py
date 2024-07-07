def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input('Enter the item to add: ')
            result = shopping_list.append(item)
            pass
        elif choice == '2':
            item = input('Enter the item to remove: ')
            result = shopping_list.remove(item)
            pass
        elif choice == '3':
            result = print(shopping_list)
            pass
        elif choice == '4':
            result = print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    return result

main()
