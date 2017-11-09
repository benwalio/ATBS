# create a number game

from random import randint
import sys

secret_num = randint(1,50)
guess = 0
guess_count = 0

while guess <> secret_num:
   guess_count += 1
   guess = raw_input("What is your guess? ")
   try:
      guess = int(guess)
   except:
      print("that isn't a number -_-\nyou lose")
      sys.exit()

   if guess > secret_num:
      print("Too high")
      continue
   elif guess < secret_num:
      print("Too low")
      continue
   else:
      print("correct! You won in " + str(guess_count) + " guesses!")
