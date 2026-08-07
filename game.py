number = input("You are in a maze pick a path 1-3: ")

if number == "1":
    print("You went left")
    choice = input("Pick a door 1-2: ")
    if choice == "1":
        print("You came across a hole and fell, congratulations!")
    elif choice == "2":
        print("There is a straight path, do you want to walk through it?")
        answer = input("Yes or No: ")
        if answer == "Yes":
            print("You walked on and on hoping for an exit but you ended up dying from physical overextertion.")