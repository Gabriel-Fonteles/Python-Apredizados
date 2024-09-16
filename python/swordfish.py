while True:
    name = input("Please enter your name: ")

    if name != 'Joe':
        continue

    password = input(f"Hello, {name}. Please enter the password: ")

    if password == 'swordfish':
        print(f"Access granted for {name}.")
        break
    else:
        print("Incorrect password. Please try again.")