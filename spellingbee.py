score = 0
percentage = 0

print("Welcome to spelling bee")
print("--- Round 1 of 4 ---")
print("Hint: A long yellow fruit")
spelling = input("Your guess: ")
if spelling.lower() == "banana":
    print("Correct!")
    score += 1
    percentage += 25
else:
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
print(f"Your final score: {score} / 4 ({percentage}%)")