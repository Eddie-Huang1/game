score = 0
percentage = 0

print("Welcome to spelling bee")
print("--- Round 1 of 3 ---")
print("Hint: A long yellow fruit")
spelling = input("Your guess: ")
if spelling == "banana":
    print("Correct!")
    score += 1
    percentage += 33.33
else:
    spelling != "banana"
    print("Incorrect, the answer is banana")

print("--- Round 2 of 3 ---")
print("Hint: A food that comes in a square box, has the shape of a circle and is cut in triangles")
spelling = input("Your guess: ")
if spelling == "pizza":
    print("Correct!")
    score += 1
    percentage += 33.33
else:
    spelling != "pizza"
    print("Incorrect, the answer is pizza")

print("--- Round 3 of 3 ---")
print("Hint: Full name of DNA")
spelling = input("Your guess: ")
if spelling == "deoxyribonucleic acid":
    print("Correct!")
    score += 1
    percentage += 33.33
else:
    spelling != "deoxyribonucleic acid"
    print("Incorrect, the answer is deoxyribonucleic acid")

print("--- GAME OVER ---")
percentage += 0.01
print(f"Your final score: {score} / 3 ({percentage}%)")