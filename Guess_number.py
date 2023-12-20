import random
print ("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")

# Generate a random number between 1 and 100
number = random.randint(1, 100)

level = input("Choose a difficulty level. Type 'easy' or 'hard'.:")
guess = 0


def guessing(guess):
  
  if number > guess:
    return "Too low"
  elif number < guess:
    return "Too high"
  else:
    return "You got it!"
if level == "easy":
  
  guess = int(input("Guess a number between 1 and 100: "))
  for i in range (10):
    print (guessing(guess))
    if number == guess:
      break
    else:
      guess = int(input(f"You have {10-1-i} attempts remaining to guess the number.\nMake a guess: "))


if level == "hard":

  guess = int(input("Guess a number between 1 and 100: "))
  for i in range (5):
    print (guessing(guess))
    if number == guess:
      break
    else:
      guess = int(input(f"You have {10-1-i} attempts remaining to guess the number.\nMake a guess: "))

print(f"The number was {number}.")
