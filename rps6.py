#ROCK PAPER AND SCISSORS
#this updated version uses f-strings.

import sys
import random  #we want ki jo hmara system woh bh ek choice kre between 1, 2 and 3 because our system is playing as opponent. toh our system needs to make choices too which are completely random and unpredictable. yeh perform krane k liye we import random module which contains random function.
from enum import Enum #this displays the value corresponding to the integer. if we want print you chose rock or python chose scissors we would need Enum.
def rps(): # afunction which wraps the whole play_rps and acts as a parent function.
    game_count=0 #global variable.
    player_wins=0
    python_wins=0
    def play_rps(): #ek function create kiya hai which is responsible for playing game.
        nonlocal player_wins #calling the variables from parent function.
        nonlocal python_wins
        
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
        print(f"You chose\t {str(RPS(player)).replace('RPS.','').title()}.") #we need to use playerchoice instead of player coz uska datatype string hai and concatenation happens between strings
        #RPS string value print krega corresponding to the no chosen. replace hm isliye use kr rhe hai qk bina replace k output is like rps.rock which is not good looking. to remove rps. we use replace and switch it with whitespace. 
        #.title is a method which capitalizes first letter and converts all other characters to lower case.
        print(f"Python chose\t {str(RPS(computer)).replace('RPS.','').title()}.\n") #we used computer_choice qk uska datatype string hai.
        print("")
        #to keep a count of who won how many times we will use nested functions.
        def decide_winner(player,computer):
            nonlocal player_wins #as this is a nested function inside the nested function play_rps, we need to again call player_wins so that we can modify it in decide_winner and access it outside of decide_winner function.
            nonlocal python_wins
        #compare who won
            if player == 1 and computer ==3:
                player_wins+=1
                return "You Win!🍾🍾" #we have replaced print with return to store the value of the result rather than just displaying it for the later use in decide_winner function
            elif player == 2 and computer ==1:
                player_wins+=1

                return "You Win!🍾🍾" #we have replaced print with return to store the value of the result rather than just displaying it for the later use in decide_winner function.
            elif player == 3 and computer ==2:
                player_wins+=1

                return "You Win!🍾🍾" #we have replaced print with return to store the value of the result rather than just displaying it for the later use in decide_winner function
            elif player==computer:
                return "Tie Game!🤗" #we have replaced print with return to store the value of the result rather than just displaying it for the later use in decide_winner function
            else:
                python_wins+=1
                return "Python Wins!🤡" #we have replaced print with return to store the value of the result rather than just displaying it for the later use in decide_winner function
        #to count the no of games we have played.
        game_result= decide_winner(player,computer) #storing the values in game_result
        print(game_result)
        nonlocal game_count #updated this from global to nonlocal because now this is a varibale of parent function and not a global variable.
        game_count+=1 #we are updating this after every game we play.
        print(f"\n Game count:  {str(game_count)}") #output to print how many times we have played the game. 
        print(f"\n Player wins:  {str(player_wins)}") #output to print how many times player won the game.
        print(f"\n Python wins:  {str(python_wins)}") #output to print how many times python won the game.
        #we have typecasted python_wins to string for concatenation purpose.
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

    return play_rps

play= rps() #play will store the return value of parent function rps().
play()