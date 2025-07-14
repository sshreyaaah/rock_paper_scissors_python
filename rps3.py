#ROCK PAPER AND SCISSORS
#this updated version contains functions and recursions..

import sys
import random  #we want ki jo hmara system woh bh ek choice kre between 1, 2 and 3 because our system is playing as opponent. toh our system needs to make choices too which are completely random and unpredictable. yeh perform krane k liye we import random module which contains random function.
from enum import Enum #this displays the value corresponding to the integer. if we want print you chose rock or python chose scissors we would need Enum.
def play_rps(): #ek function create kiya hai which is responsible for playing game.
    
    
    #this assigns string value to each integer.
    class RPS(Enum):
        ROCK=1
        PAPER=2
        SCISSORS=3
    

    playerchoice= input("Enter...\n1. for Rock,\n2. for Paper,\n3. for Scissors:\n\n") #asks for user input
    if playerchoice not in ["1","2","3"]: #agr hmare user ne options k alawa kuch or input diya hai.
        print("you must enter 1, 2 or 3.")
        return play_rps() #recursive call to the function again after telling user to only enter 1,2,3. this will automatically restart the game.
    
    player= int(playerchoice) #hmne typecasting ki hai qk hmara user input string datatype ka hai and logical operators integer datatype pr kaam krte hai.

    computer_choice=random.choice("123") #this is the random choice made by the computer amongst 1,2 or 3. The computer is randomly going to choose one character from the string 123.
    computer=int(computer_choice) #the choice made by computer is also string isliye typecasting krenge.

    #display the choices made
    print("")
    print("You chose\t"+ str(RPS(player)).replace('RPS.','')+".") #we need to use playerchoice instead of player coz uska datatype string hai and concatenation happens between strings
    #RPS string value print krega corresponding to the no chosen. replace hm isliye use kr rhe hai qk bina replace k output is like rps.rock which is not good looking. to remove rps. we use replace and switch it with whitespace.
    print("Python chose\t"+ str(RPS(computer)).replace('RPS.','')+".") #we used computer_choice qk uska datatype string hai.
    print("")

    #compare who won
    if player == 1 and computer ==3:
        print("You Win!🍾🍾")
    elif player == 2 and computer ==1:
        print("You Win!🍾🍾")
    elif player == 3 and computer ==2:
        print("You Win!🍾🍾")
    elif player==computer:
        print("Tie Game!🤗")
    else:
        print("Python Wins!🤡")
    print("\n Play again?")
    while True:
        playagain=input("\n Y for yes or \n Q for quit \n\n") #asks for user input otherwise it will be an endless loop where the system will play the game.
        if playagain.lower() not in ["y","q"]: #again agr user ne options k alawa kuch or select kiya toh hm system dubara se puchega ki yes or quit. we can only quit the game using q and not by any other char. which could be done previously.
            continue
        else:
            break
    if playagain.lower() == "y": #lowecase the input. if user enters capitals.
        return play_rps()
    else:
        print("\n🥂🥂")
        print("Thankyou!\n")
        sys.exit("Bye! 👋")

play_rps() #function call