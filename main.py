import csv
import random


def get_random_word():
  with open('words.csv', 'r') as csvfile:
    # Create a reader object
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
      if csv_reader.line_num == 1:
          continue 
      if random.random() > 0.7:
          return row
      
def hide_word(word):
  hidden_word = ""
  for index in range(len(word)):
    if index == 0:
      hidden_word += word[index]
    else:
      hidden_word += "*"
  return hidden_word

def show_letter(letter, hidden_word, word):
  replaced_word = ""
  if letter in word:
    for index in range(len(word)):
      if word[index] == letter:
        replaced_word += letter
      elif hidden_word[index] == "*":
        replaced_word +="*"  
      else:
        replaced_word += hidden_word[index]
    return replaced_word
  else:
    return hidden_word
            

word_selected = get_random_word()
word = word_selected[0]
hint = word_selected[1]
hidden_word = hide_word(word)
letter_guesses = 0
tries_remaining = len(word) + 3

print(hidden_word)
print(hint)

while True:
  print(f"You have {tries_remaining} guesses.")
  hidden_word = show_letter(input("Enter a letter --> "), hidden_word, word)
  print(hidden_word)
  letter_guesses += 1
  tries_remaining -= 1
  if(hidden_word == word):
    print(f"Congratulations! You found all the letters in the word! You guessed {letter_guesses} letters.")
    break
  elif(tries_remaining == 0):
    print("Sorry, you ran out of guesses!")
    break