# shopping_list_manager.py

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
            # Prompt for and add an item
            item_to_add=input("Enter Item to add to the list :")
            shopping_list.append(item_to_add)
            print(f" >> {item_to_add} >> has been added to the list successfuly !")
            pass
        elif choice == '2':
            # Prompt for and remove an item 
            item_to_remove=input("Enter item to remove from the list : ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"<< {item_to_remove} >> has been removed from the shopping list ")
            

            pass
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\n Your shopping List :")
                for item in shopping:
                    print(f" >> {item} ")
            else:        
                print("\n Your shopping list is empty ! ")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()