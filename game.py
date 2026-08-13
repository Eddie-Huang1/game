number = input("You are in a maze pick a path 1-3: ")

if number == "1":
    print("You went left")
    choice = input("There is two heavy doors, pick 1-2: ")
    if choice == "1":
        print("You came across a hole and fell, congratulations!")
    elif choice == "2":
        print("There is a straight path, do you want to walk through it?")
        answer = input("yes or no: ")
        if answer == "yes":
            print("You walked on and on hoping for an exit but you ended up dying from physical overextertion.")
        elif answer == "no":
            print("You are now stuck forever because the door trapped you in.")

elif number == "2":
    print("You went straight")
    choice = input("left or right: ")
    if choice == "left":
        print("There is only one correct path, good for you, this isn't the correct one, you died to a trap")
    elif choice == "right":
        print("You have came across a bridge with a river underneath")
        print("Want to cross it?")
        answer = input("yes or no: ")