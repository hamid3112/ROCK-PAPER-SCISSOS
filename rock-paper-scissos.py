قخ#import and  global varibale 

import random
user_choice = ("rock" , "paper" , "scissor")



# create a function to get usr input

def get_user_input():
    choice = input("enter your choice (\"rock\" , \"paper\" , \"scissor\"): ")
    while choice not in user_choice:
        choice = input("enter your choice (\"rock\" , \"paper\" , \"scissor\"): ")
    return choice

#create a function to get pc input

def get_pc_input():
    pc_choice = random.choice(user_choice)
    print(f"pc choice is : {pc_choice}")
    return pc_choice


#copmare and determine witch one is the winner

def determine_winner (user_input , pc_input):
    if user_input == pc_input:
        return "draw" 
    elif (user_input =="rock" and pc_input == "scissor")\
          or (user_input =="scissor" and pc_input == "paper")\
          or (user_input =="paper" and pc_input == "rock"):
        return "user won"   
    else:
        return "pc won"





#create a main function as the runner

def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    result = determine_winner(user_input , pc_input)
    return result

#make an iteration for doing the game as much as we need.
answer = "y"
pc_win=0
user_win=0
while answer == "y":
    result = main()
    if result =="user won":
        user_win+=1
    elif result =="pc won":
        pc_win+=1
    print (result)
    print(f"user win:{user_win}\npc win:{pc_win}")
    answer = input("do you want to countinu(y/n): ")