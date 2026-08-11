print("Welcome to spelling bee")
print("--- Round 1 of 3 ---")
print("Hint: A long yellow fruit")
spelling = input("Your guess: ")
if spelling == "banana":
    print("Correct!")
else:
    spelling != "banana"
    print("Incorrect, the answer is banana")

print("--- Round 2 of 3 ---")
print("Hint: A food that comes in a square box, has the shape of a circle and is cut in triangles")
spelling = input("Your guess: ")
if spelling == "pizza":
    print("Correct!")
else:
    spelling != "pizza"
    print("Incorrect, the answer is pizza")

print("--- Round 3 of 3 ---")
print("Hint: Supermans weakness")
spelling = input("Your guess: ")
if spelling == "kryptonite":
    print("Correct!")
else:
    spelling != "kryptonite"
    print("Incorrect, the answer is kryptonite")

print("--- GAME OVER ---")