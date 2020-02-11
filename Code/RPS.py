# import random module 
import random
# import time module
import time

print("ROCK PAPER SCISSORS")

# Allow program to pause for 1.5 Seconds
time.sleep(1.0)

while True: 
    print("\nMake your choice \n Press 1 for Rock \n Press 2 for paper \n Press 3 for scissor \n") 
      
    # take the input from user 
    choice = int(input("Enter: "))
      
    # loop until user enters valid input 
    while choice > 3 or choice < 1: 
        choice = int(input("\nChoose the right option: ")) 
          
  
    # initialize choice_name to choice_value 
    if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'
          
    # print user choice  
    print("\nYour choice is: " + choice_name)

    time.sleep(1.0)
    
    print("\nReady ?")

    time.sleep(1.0)

    print("\nRock!")
    time.sleep(0.5)
    print("\nPaper!")
    time.sleep(0.5)
    print("\nScissors!")
    time.sleep(0.5)
    print("\nShoot!\n")
  
    # Computer randomly chooses any number  
    # among 1 , 2 and 3. Using randint method 
    # of random module 
    comp_choice = random.randint(1, 3) 

    #print(comp_choice) 
  
    # initialize value of comp_choice_name  
    # variable corresponding to the choice value 
    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          

    print(choice_name + " V/s " + comp_choice_name)
    print("\t")

    time.sleep(1.0)

    # condition for winning 
    if((choice == 1 and comp_choice == 1) or
      (choice == 2 and comp_choice ==2) or (choice == 3 and comp_choice == 3)): 
        print("<===Tie===> ", end = "") 
        result = "tie"

    elif((choice == 1 and comp_choice == 2) or
        (choice == 2 and comp_choice ==1 )): 
        print("<===Paper wins===> ", end = "") 
        result = "paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("<===Rock wins===>", end = "") 
        result = "Rock"
    else: 
        print("<===Scissor wins===>", end = "") 
        result = "scissor"
  
    # Printing either user or computer wins 
    if result == "tie": 
        print("\n")
    elif  result == choice_name:
        print("<=== You won ===>\n")
    else: 
        print("<=== Computer won ===>\n")

    time.sleep(0.5)
    print("Computer's choice was : " + comp_choice_name + "\n") 

    print("Go again? (Y/N)") 
    ans = input() 
  
  
    # if user input n or N then condition is True 
    if ans == 'n' or ans == 'N': 
        break
