
def display_menu():
    print("The shopping List Manager:")
    print(" 1. Add item. ")
    print(" 2. Remove item. ")
    print(" 3. View List. ")
    print(" 4. Exit. ")


def main():

    shopping_list = []
    while True:
        display_menu()
        choice = input(" Enter Your choice:")
        if choice == '1':
            item_to_add = input("Enter a new item to the list :")
            shopping_list.append(item_to_add)
            print(
                f" >>>: {item_to_add} has been added to the list successfully! ")
            pass
        elif choice == '2':
            item_to_remove = input(" Enter item to remove : ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(
                    f" <<<: {item_to_remove} :>>> has been removed from the list successfully !")
            else:
                print(
                    f" >>>: {item_to_remove} was not found on the shopping list !")
            pass
        elif choice == '3':
            if shopping_list:
                print("\n Your shopping_list")
                for item in shopping_list:
                    print(f" >> {item}")
            else:
                print("\n your shopping list is empty. ")
            pass
        elif choice == '4':
            print("Thank you, GoodBye!!! ")
            break
        else:
            print(" Invalid choice , try Again!!")


main()

if __name__ == "__main ":
    main()
