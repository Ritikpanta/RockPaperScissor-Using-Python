import random 
print("")
print("Welcome to the code of the rock paper scissor ")
user = input("choose your choice \n1.rock \n2.paper \n3.scissor : ")
if user == "rock" or "paper" or "scissor":
 choices = [ "rock","paper","scissor"]
 computer = random.choice(choices)
 print(f"YOU = {user} \nCOMPUTER = {computer}")

if user == "rock" and computer == "paper" or user == "paper" and computer == "scissor" or user == "rock" and computer == "scissor":
    print("COMPUTER LOST, YOU WON")

elif user == "paper" and computer == "scissor" or user == "rock" and computer == "paper" or user == "scissor" and computer == "rock":
    print("YOU LOST COMPUTER WON")
if user ==  computer :
    print("WOAH it is a tie ")
else: 
    print("Write right input you dumbhead")

    

