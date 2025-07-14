#ROCK PAPER AND SCISSORS

import sys
import random  #we want ki jo hmara system woh bh ek choice kre between 1, 2 and 3 because our system is playing as opponent. toh our system needs to make choices too which are completely random and unpredictable. yeh perform krane k liye we import random module which contains random function.
from enum import Enum #this displays the value corresponding to the integer. if we want print you chose rock or python chose scissors we would need Enum.

#this assigns string value to each integer.
class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

playerchoice= input("Enter...\n1. for Rock,\n2. for Paper,\n3. for Scissors:\n\n") #asks for user input
player= int(playerchoice) #hmne typecasting ki hai qk hmara user input string datatype ka hai and logical operators integer datatype pr kaam krte hai.
if player<1 or player>3:     # if the player enters a value which is not in the option then we need the system to exit.
    sys.exit("you must enter 1, 2 or 3.")  #sys.exit is a function which helps to exit the code if the conditions are not met.
                                           #agr hm yha pr sys.exit ki jgh print statement use krte toh hmara code you must..... to print kr deta lekin code se exit nh krta jiski wjh se jo following loc hai woh execute ho jate but iss case mein hme system exit krana hai agr hmara code kaam nh kr rha hai toh.

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
    