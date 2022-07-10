import time

from keywords import (
    YES,
    NO,
    OPEN,
    CARRY_ON,
    BLUE,
    RED,
    ANSWER,
    IGNORE,
    UP,
    DOWN
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
        print_text("Great. You are currently in your family home.", 2)
        print_text("However not the one you know of.", 2)
        print_text("The interior looks different.", 2)
        print_text("You scan the room and see several unfamiliar items,", 2)
        print_text("such as various paintings on vintage, floral wallpaper", 2)
        print_text("Your hear a noise in the room next door.", 2)
        print_text("A banging and sounds of moved items across a surface", 2)
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
        print_text("'otherwise you'll be stuck in this time period.'", 2)
        print_text("She opens a drawer of her bedside table", 2)
        print_text("and pulls out a flask with a yellowish substance.", 2)
        print_text("'Drink this and try to sleep,'", 2)
        print_text("'we'll see each other again at some point'", 2)
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
        print_text("You walk along the corridor", 2)
        print_text("and you suddenly hear knocking at the front door.", 2)
        open_or_not()


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
        print_text("", 1)
        print_text("The time capsule couldn't take the pressure", 2)
        print_text("", 1)
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


def open_or_not():
    '''
    The user can decide whether to open the door or not in the game.
    This function uses the "answer" and "ignore" keywords.
    '''
    print("Will you open the door? (answer/ignore)")
    response = input("")

    while response not in [ANSWER, IGNORE]:
        print_text("Response is invalid, please try again", 2)
        response = input("")
    if response in ANSWER:
        print_text("You walk down the stairs and towards the front door", 2)
        print_text("You open the door and see no one.", 2)
        print_text("Instead of a person you spot a parcel", 2)
        print_text("on the ground.", 2)
        print_text("You see your name written in beautiful,", 2)
        print_text("cursive handwriting on the brown wrapping paper.", 2)
        print_text("Upon opening the package you realise", 2)
        print_text("it held a watch. It has a golden crown on the side", 2)
        spin_up_or_down()
    elif response in IGNORE:
        print_text("You head to the garden", 2)
        print_text("and spot a large shed in the corner", 2)
        print_text("When entering you notice a huge metal construction", 2)
        print_text("You also spot it has an entrance", 2)
        print_text("You step inside and find two different", 2)
        print_text("coloured levers", 2)
        blue_or_red()


def spin_up_or_down():
    '''
    This function operates through the "up" and "down" keywords.
    '''
    print("Do you want to spin the crown up or down?")
    response = input("")

    while response not in [UP, DOWN]:
        print_text("Response is invalid, please try again", 2)
        response = input("")
    if response in UP:
        print_text("You spin upwards.", 2)
        print_text("Your surroundings become blurred.", 2)
        print_text("You start to sway and realise", 2)
        print_text("you can no longer hold yourself up.", 2)
        print_text("Your vision goes fully black.", 2)
        print_text("...", 2)
        print_text("", 1)
        print_text("", 1)
        print_text("When you open your eyes you recognise your home;", 2)
        print_text("However when you look down at the watch", 2)
        print_text("it is smashed, rusty and looks nothing like", 2)
        print_text("it did in the 1920s from which you came.", 2)
        print_text("You made it back, congratulations", 2)
        start_again()
    elif response in DOWN:
        print_text("You spin upwards.", 2)
        print_text("Your surroundings become blurred.", 2)
        print_text("You start to sway and realise", 2)
        print_text("you can no longer hold yourself up.", 2)
        print_text("Your vision turns fully black.", 2)
        print_text("...", 2)
        print_text("", 1)
        print_text("", 1)
        print_text("When you open your eyes you are still lying down", 2)
        print_text("in the hallway", 2)
        print_text("The bright green wallpaper draws your attention", 2)
        print_text("as it's different from the previous 1920 decor", 2)
        print_text("You check the newspaper on top of the", 2)
        print_text("large table on the side.", 2)
        print_text("23.06.1962", 2)


def main():
    '''
    This function runs the game and all the other functions
    '''


begin_game()

if __name__ == '__main__':
    main()
