import keyboard
import os
import random

def start_menu(): 
 # Prints out the menu and redirects the user to the option it types in.
  os.system("cls" if os.name == "nt" else "clear")  
  print("[1] Play game"),
  print("[2] Rules"), 
  print("[3] Quit")
  
  start_menu_choice = input()
  
  if start_menu_choice == "1":
    main()
  elif start_menu_choice == "2":
    print_rules()
  elif start_menu_choice == "3":
    exit()
  else:
    print("Invalid choice please enter a valid number") 
    start_menu()

def print_rules():
  # Prints the basic rules for the game.
  os.system("cls" if os.name == "nt" else "clear")
  print("Mastermind rules:")
  print("Your jobb is to guess the 4 color code, You have 10 tries.")
  print("The colors that the code could be made up with are: Red, Green, Blue, Yellow, Orange and Pink. The same color can occur more than once.")
  go_back = input("Would you like to go back to the menu? (Yes or No) ") 
  
  if go_back.lower() == "yes":
    start_menu()
  else: 
    os.system("cls" if os.name == "nt" else "clear")
    print_rules()

def correct_code():
  # Generates the a random 4 color code out of the 6 colors in the "colors" list
  colors = ["Red", "Green", "Blue", "Yellow", "Orange","Pink"]
  color_1 = random.choice(colors)
  color_2 = random.choice(colors)
  color_3 = random.choice(colors)
  color_4 = random.choice(colors)
  
  correct_code = [color_1, color_2, color_3, color_4]
  # print(correct_code) (For debugging)
  return correct_code

def code_guess():
  # Gets the users guess
  user_guess = input("Enter your guess, the possible colors are as follows (Red, Green, Blue, Yellow, Orange and Pink). Please use spaces inbetween your 4 colors: ")
  guess = user_guess.split()
  return guess

def check_guess(guess, correct_code):
  # First checks if the color is the right color *and* in the right position, if not, checks if its in the code at all.
  print(guess)
  for i in range(0, 4):
    if guess[i] == correct_code[i]:
      print(f"{guess[i]} is in the code and in the correct possition {i+1}")
    elif guess[i] in correct_code:
      print(f"{guess[i]} is in the code but not in the correct possition {i+1}")
    else:
      print(f"The color {guess[i]} is not in the code")

def check_win(guess, correct_code):
  # Win condition - Self explanatory 
  return guess == correct_code

def main():
  # Runs the main game
  tries = 0
  playing = True
  correct = correct_code() 
  while playing is True:
    tries += 1
    if __name__ == "__main__":
      guess = code_guess()
      win_condition = check_win(guess, correct)
      os.system("cls" if os.name == "nt" else "clear")
      if win_condition is True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Your guess was {guess}")
        print(f"You won! It took {tries} tries")
        playing = False
      else:
        check_guess(guess, correct)
        
    if tries == 10:
      print(f"You lost! It has been 10 tries and you have not guessed the code. The code is {correct} your last guess was {guess}")

start_menu()