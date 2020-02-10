import random
  
# Randomly choose correct_answer
a = 1
b = int(input("Enter max limit: "))
correct_answer = random.randint(a, b)
# print("Debugging Aid: winning_number is '{}'".format(winning_number))  
  
# Limits user to four guesses
guesses_remaining = int(input("\nEnter the number of guesses you want: "))
  
print("\nYou have {} attempts to guess the correct number. Give it a shot!".format(guesses_remaining))
  
 
while  guesses_remaining > 0:
 
    while True:
        try:
            guess = int(input("\nGuess a number between 1 and {}: ".format(b)))
            if a <= guess <= b:
                break     #Exit 'while True' loop
            else:
                print("Your guess was NOT a number between 1 and {}.  Try again.".format(b))
        except:
            print("Your guess was NOT an Integer.  Try again.")
     
 
    # Decrease guess counter by one each time to limit to four guesses.
    guesses_remaining -= 1
    if guess == correct_answer:
        print ("\nCongratluations! You guessed the correct number. ")
        guesses_remaining = 0     # End game after correct guess.
    elif guesses_remaining == 0:
        print ("\nYou are out of tries! The winning number was:",correct_answer, "\n\nBetter luck next time!")
    elif guesses_remaining == 1:
        print("\nSorry, that is not the correct number. Try again!  You have one try remaining.")
    else:
        print("\nSorry, that is not the correct number. Try again!  You have {} tries remaining.".format(guesses_remaining))
