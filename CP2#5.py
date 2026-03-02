users = []

while True:
    print("\n1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(users)

    elif choice == "2":
        add = input("Add new user: ")
        users.append(add)
        print(users)

    elif choice == "3":
        update = input("Which user do you want to update? ")

        if update in users:
            index = users.index(update)
            new_value = input("Enter new name: ")
            users[index] = new_value

        print(users)

    elif choice == "4":
        remove = input("Select and delete a user: ")

        if remove in users:
            users.remove(remove)

        print(users)

    elif choice == "5":
        break