import time

from keywords import(

    YES,
    NO
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
    print_text("Find your way to a time machine that will take you back...", 1)
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

    elif response in NO:
        print_text("Goodbye, thanks for coming.", 2)
        start_again()


begin_game()


# def run():

    # '''
    # This function integrates all the other functions and runs the game
    # '''


# run()




