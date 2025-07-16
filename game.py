import random 

choices = ["r", "p", "s"]

def get_user_choice():
    while True:
        user_choice = input("Give your input (R/P/S): ").lower()
        if user_choice in choices:
            print(f"Your choice was: {user_choice}" )
            return user_choice
        elif user_choice != choices:
            print("please choose a valid option")    
    
def get_comp_choice():
    comp_choice = random.choice(choices)
    print(f"computer chose: {comp_choice}" )
    return comp_choice
    
def get_the_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        print("its a tie!")
    elif user_choice == "p" and comp_choice == "r" or \
       user_choice == "s" and comp_choice == "p" or \
       user_choice == "r" and comp_choice == "s":
        print("You won the game! hurrah!!")
    else:
        print("try again later!")
       
while True:
    user = get_user_choice()
    comp = get_comp_choice()
    get_the_winner(user, comp)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
        