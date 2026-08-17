# Variables
score = 0
percentage = 0

print("Welcome to spelling bee")
print("--- Round 1 of 4 ---")
print("Hint: A long yellow fruit")
spelling = input("Your guess: ")
# Using .lower() to make sure that even if you use capital letters, the answer is still right
if spelling.lower() == "banana":
    print("Correct!")
    # Adding score and percentage if you get it right
    score += 1
    percentage += 25
else:
    # Telling them that they are wrong and showing them the answer
    spelling != "banana"
    print("Incorrect, the answer is banana")

print("--- Round 2 of 4 ---")
print("Hint: A food that comes in a square box, has the shape of a circle and is cut in triangles")
spelling = input("Your guess: ")
if spelling.lower() == "pizza":
    print("Correct!")
    score += 1
    percentage += 25
else:
    spelling != "pizza"
    print("Incorrect, the answer is pizza")

print("--- Round 3 of 4 ---")
print("Hint: Full name of DNA")
spelling = input("Your guess: ")
if spelling.lower() == "deoxyribonucleic acid":
    print("Correct!")
    score += 1
    percentage += 25
else:
    spelling != "deoxyribonucleic acid"
    print("Incorrect, the answer is deoxyribonucleic acid")

print("--- Round 4 of 4 ---")
print("Hint: Fear of long words")
spelling = input("Your guess: ")
if spelling.lower() == "hippopotomonstrosesquippedaliophobia":
    print("Correct!")
    score += 1
    percentage += 25
else:
    spelling != "hippopotomonstrosesquippedaliophobia"
    print("Incorrect, the answer is hippopotomonstrosesquippedaliophobia")

print("--- GAME OVER ---")
# Adding up the final score and showing them the percentage that they got
print(f"Your final score: {score} / 4 ({percentage}%)")