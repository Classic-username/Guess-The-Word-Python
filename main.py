import csv
import random

word = None
hint = None

with open('words.csv', 'r') as csvfile:
  # Create a reader object
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        print(csv_reader.line_num)
        if csv_reader.line_num == 1:
            continue 
        word = row[0]
        hint = row[1]
        if random.random() > 0.7:
            break

print(word)
print(hint)

# The below code is commented, I plan to implement some of this logic into the word game above.
# import random
# number = random.randint(1, 100)
# is_game_over = False
# tries = 0

# print("Hello, welcome to Guess the Number!")
# print("I'm thinking of a number between 1 and 100, try to guess...")
# while not is_game_over:
#     guess = int(input("Enter a number... "))
#     tries += 1
#     if guess < number:
#         print("The number is higher")
#     elif guess > number:
#         print("The number is lower")
#     else:
#         is_game_over = True

# print(f"Excellent, you guessed in {tries} tries, the number is {number}")