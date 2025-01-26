import random as rnd # This is the random module  
allowed_values : list[str] = ["rock", "paper", "scissors"] # These are the allowed values   
for i in allowed_values :  
    print(i)    
user_choice : str  = input("enter user choice\n") # This is the user's choice    
computer_choice : str =   rnd.choice(allowed_values) # This is the computer's choice
print("computer choice is " + computer_choice)
if user_choice not in allowed_values :  # {
    print("Invalid choice")  
    quit()  
#}
if computer_choice == user_choice :
    print("tie")
elif computer_choice == "rock":
    if user_choice == "scissors" :
        print("computer wins")  
    if user_choice == "paper" :        
        print("user wins")  
elif computer_choice == "scissor" :
    if user_choice == "paper" :         
        print("computer  wins")      
    if user_choice == "rock" :        
        print("user wins")  
elif computer_choice == "paper" : 
    if user_choice == "rock" : 
        print("computer wins")  
    if user_choice == "scissors" : 
        print("user wins")  
else :
    print("invalid choice")     

