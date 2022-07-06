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

def begin_game():
    print("Welcome to the journey. Would you like to begin? (yes/no)")
    response = input("")
    while response not in [YES, NO]:
        print_text("Please enter a valid response", 2)
        response = input("")
    if response in YES:
        print_text("Let's begin!", 2)

    name = input("What's your name?\n")
    print(f"Hi {name}!")

begin_game()

# def run():
    # '''
    # This function integrates all the other functions and runs the game
    # '''


# run()




