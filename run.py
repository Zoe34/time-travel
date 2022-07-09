import time

from keywords import(

    YES,
    NO,
    OPEN,
    CARRY_ON
)

def print_text(text: str, delay: int):
    '''
    Function prints text after user input
    '''
    print(text)
    time.sleep(delay)

def start_again(): 
    '''
    Game begins again when the user decides to quit once asked "Are you ready?" 
    '''
    begin_game()


def begin_game():
    '''
    This function runs the game and all the main questions for the user are 
    placed here.
    '''
    print("Welcome to the journey. Would you like to begin? (yes/no)")
    response = input("")
    while response not in [YES, NO]:
        print_text("Please enter a valid response", 2)
        response = input("")
    if response in YES:
        print_text("Let's begin!", 2)
    elif response in NO:
        print_text("Goodbye, thanks for coming:", 2)
        start_again()

    name = input("What's your name?\n")
    print_text(f"Hi {name}!", 1)
    print_text("You have time travelled to the past.", 1)
    print_text("You are looking for a way home.", 1)
    print_text("Are you ready? (yes/no)", 1)
    response = input("")

    while response not in [YES, NO]:
        print_text("Please enter a valid response", 2)
        response = input("")

    if response in YES:
        print_text("Great. You are currently in your family home.", 1)
        print_text("However not the one you know of.", 1)
        print_text("The interior looks different.", 1)
        print_text("You scan the room and see several unfamiliar items,", 1)
        print_text("such as various paintings on vintage, floral wallpaper", 1)
        print_text("Your hear a noise in the room next door.", 1)
        print_text("A banging and the sound of moved items across a surface", 1)
    
    elif response in NO:
        print_text("Goodbye, thanks for coming.", 2)
        start_again()
        
    print("Do you want to open the door or carry on?\n")
    print("open/carry on\n")
    response = input("")

    while response not in [OPEN, CARRY_ON]:
        print("Response is invalid")
        response = input("")
    if response in OPEN:
        print_text("You open the door and find an older woman.", 1)
        print_text("She has her back to you", 1)
        print_text("She appears to be wiping down the surface of her bedside table", 1)
        print_text("She doesn't notice you until a few seconds later", 1)
        print_text("The woman looks very familiar.", 1)
        print_text("Her facial features look very similar to that of yourself.", 1)
        print_text("You realise this is your great great grandmother", 1)
        print_text(f"'Oh I was expecting you {name}'", 1)
        print_text("She looks very pleased to see you.", 1)
        print_text(f"'We need to hurry up {name}, otherwise you'll be stuck in this time period.'", 1)
        print_text("She opens a drawer of her bedside table and pulls out a flask with a yellowish substance.", 1)
        print_text("'Drink this and try to sleep, we'll see each other again at some point'", 1)
        print_text("She gives you a warm smile and leaves the room, closing the door.", 1)
    elif response in CARRY_ON:
        print_text("You walk downstairs", 1)
        print_text("You walk towards what seems to be the kitchen", 1)
        print_text("and open the door", 1)
        print_text("The kitchen looks exatly like the room upstairs", 1)
        print_text("In fact it is the same room", 1)
        print_text("It's as though you never left that room...", 1)

    while response in CARRY_ON:
        


begin_game()


# def run():

    # '''
    # This function integrates all the other functions and runs the game
    # '''


# run()




