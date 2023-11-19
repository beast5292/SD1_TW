def fill_spaces(spaces):
  word = ''
  for guesses in spaces:
    word += guesses
  print(word)

def same_elements(secret_list,user_guess):
  multiple = False
  indexes = [same for same in range(len(secret_list)) if secret_list[same] == user_guess ]
  if len(indexes) > 1:
    multiple = True

  return multiple,indexes

def guessed(spaces,secret,finished_guessing):
  guessed_word = ''
  for i in spaces:
    guessed_word += i
  
  if guessed_word == secret:
    finished_guessing = True
  
  return finished_guessing


def gussed_count(user_guess,secret_list,turns):
  if user_guess not in secret_list:
    turns -= 1
  
  return turns



finished_guessing = False
secret = 'starship'   
secret_list = [element for element in secret]
spaces = ['-' for i in range(len(secret))]
turns = len(secret) + 1

print("Let's play Guess the Word")
print(f"You have {turns} turns to guess the word!")
print('-'*len(secret))

while(turns != 0 and finished_guessing != True):
  user_guess = input("Enter your guess: ").lower()

  if user_guess in secret:
    multiple,indexes = same_elements(secret_list,user_guess)

    if multiple == True:
      for elements in indexes:
        spaces[elements] = user_guess
      fill_spaces(spaces)
      turns = gussed_count(user_guess,secret_list,turns)
    else:
      index = secret.index(user_guess)
      spaces[index] = user_guess
      fill_spaces(spaces)
      turns = gussed_count(user_guess,secret_list,turns)
  else:
    print("Invalid guess")
    fill_spaces(spaces)
    turns = gussed_count(user_guess,secret_list,turns)

  finished_guessing = guessed(spaces,secret,finished_guessing)
  print(f"You have {turns} more guesses")

print("\nYour guess:")
for guesses in spaces:
  print(guesses,end="")

if '-' in spaces:
  print("\nBetter luck next time")
elif '-' not in spaces:
  print("\nYou guessed it right!!")



