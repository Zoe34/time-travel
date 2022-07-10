import time

from keywords import(
    YES,
    NO,
    OPEN,
    CARRY_ON,
    BLUE,
    RED
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
    
    global name
    name = input("What's your name?\n")
    print_text(f"Hi {name}!", 2)
    print_text("You have time travelled to the past.", 2)
    print_text("The year is 1920", 2)
    print_text("You are looking for a way home.", 2)
    print_text("Are you ready? (yes/no)", 2)
    response = input("")

    while response not in [YES, NO]:
        print_text("Please enter a valid response", 2)
        response = input("")

    if response in YES:
        print_text("Great. You are currently in your family home.", 1)
        print_text("However not the one you know of.", 2)
        print_text("The interior looks different.", 2)
        print_text("You scan the room and see several unfamiliar items,", 2)
        print_text("such as various paintings on vintage, floral wallpaper", 2)
        print_text("Your hear a noise in the room next door.", 2)
        print_text("A banging and the sound of moved items across a surface", 2)
    
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
        print_text("You open the door and find an older woman.", 2)
        print_text("She has her back to you", 2)
        print_text("She's wiping down the surface of her bedside table", 2)
        print_text("She doesn't notice you until a few seconds later", 2)
        print_text("The woman looks very familiar.", 2)
        print_text("Her facial features look very similar to yours.", 2)
        print_text("You realise this is your great great grandmother", 2)
        print_text(f"'Oh I was expecting you {name}'", 2)
        print_text("She looks very pleased to see you.", 2)
        print_text(f"'We need to hurry up {name},'", 2)
        print_text("otherwise you'll be stuck in this time period.", 2)
        print_text("She opens a drawer of her bedside table", 2)
        print_text("and pulls out a flask with a yellowish substance.", 2)
        print_text("'Drink this and try to sleep,'", 2)
        print_text("we'll see each other again at some point", 2)
        print_text("She gives you a warm smile and leaves the room.", 2)
        print_text("You wake up but have no idea how much tme has passed.", 2)
        print_text("The room decor looks different.", 2)
        print_text("You look at the calendar.", 2)
        print_text("1962; Great the drink worked", 2)
        print_text("You get up and walk down to the only place you haven't", 2)
        print_text("explored yet: the basement", 2)
        print_text("The dark room appears to have", 2)
        print_text("a large metal construction", 2)
        print_text("Quite odd for something in a household", 2)
        print_text("The giant metal box has an entrance", 2)
        print_text("and two levers inside", 2)
        blue_or_red()

    elif response in CARRY_ON:
        print_text("You walk downstairs", 2)
        print_text("You walk towards what seems to be the kitchen", 2)
        print_text("and open the door", 2)
        print_text("The kitchen looks exatly like the room upstairs", 2)
        print_text("In fact it is the same room", 2)
        print_text("It's as though you never left that room...", 2)
        

def blue_or_red():
    '''
    Function allows user to decide whether they will pick the red or blue
    option.
    '''
    print_text("One is red, the other blue. What's your pick?", 2)
    response = input("")
    while response not in [BLUE, RED]:
        print_text("invald response, please try again", 2)
    if response in RED:
        print(f"You picked {response}")
        print_text("You have been sucked into a black hole.", 2)
        print_text("The time capsule couldn't take the pressure", 2)
        print_text("Game over.", 2)
        start_again()
    elif response in BLUE:
        print(f"You picked {response}")
        print_text("You feel the machine shaking and tumbling around.", 2)
        print_text("You wake up in the woods. The ones next to your home.", 2)
        print_text("It's impossble to tell what year it is", 2)
        print_text("So you leave the time machine in the woods", 2)
        print_text("and head to the house", 2)
        print_text("As you enter everything looks familiar.", 2)
        print_text("Your mum walks in from the living room", 2)
        print_text(f"'Hi, {name}, how was school?'", 2)
        print_text("You made your way home, congratulations!", 2)
        start_again()


begin_game()
