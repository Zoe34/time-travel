'''
The keywords used throughout the game to make choices
'''
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
    DOWN,
    LEAVE,
    EXPLORE,
    NAME,
)


def begin_game():
    '''
    This function starts the game and briefly explains the theme.
    It is called by the main() function.
    '''
    # The f string calls the user by their name
    print(f"Hi {NAME}!")
    print("Welcome to the journey. Would you like to begin? (yes/no)")
    response = input("")
    print("")
    print("")
    print("")
    print("")
    # User can input the keyword lowercase or uppercase
    while response not in [YES, NO, YES.capitalize(), NO.capitalize()]:
        print("Invalid response, please try again.")
        # User can input again here
        response = input("")
    if response in [YES, YES.capitalize()]:
        print("Let's begin!")
    if response in [NO, NO.capitalize()]:
        print("Goodbye, thanks for coming!")
        # Game ends here
        quit()

    print("You have time travelled to the past.")
    print("The year is 1920")
    print("You are looking for a way home.")
    print("Are you ready? (yes/no)")
    response = input("")
    print("")
    print("")
    print("")
    print("")

    while response not in [YES, NO, YES.capitalize(), NO.capitalize()]:
        print("Invalid response, please try again.")
        response = input("")

    if response in [YES, YES.capitalize()]:
        print("Great. You are currently in your family home.")
        print("However not the one you know of.")
        print("The interior looks different.")
        print("You scan the room and see several unfamiliar items,")
        print("such as various paintings on vintage, floral wallpaper")
        print("Your hear a noise in the room next door.")
        print("A banging and sounds of moved items across a surface")
        open_or_carry_on()
    elif response in [NO, NO.capitalize()]:
        print("Goodbye, thanks for coming!")
        quit()


def open_or_carry_on():
    '''
    Function uses OPEN and CARRY_ON keywords to allow user to make a decision.
    It is called by the begin_game() function.
    '''
    print("Do you want to open the door or carry on?\n")
    print("open/carry on\n")
    response = input("")
    print("")
    print("")
    print("")
    print("")

    while response not in [OPEN, CARRY_ON, OPEN.capitalize(),
                           CARRY_ON.capitalize()]:
        print("Invalid response, please try again.")
        response = input("")
    if response in [OPEN, OPEN.capitalize()]:
        print("You open the door and find an older woman.")
        print("She has her back to you")
        print("She's wiping down the surface of her bedside table")
        print("She doesn't notice you until a few seconds later")
        print("The woman looks very familiar.")
        print("Her facial features look very similar to yours.")
        print("You realise this is your great great grandmother")
        print(f"'Oh I was expecting you {NAME}'")
        print("She looks very pleased to see you.")
        print(f"'We need to hurry up {NAME},'")
        print("'otherwise you'll be stuck in this time period.'")
        print("She opens a drawer of her bedside table")
        print("and pulls out a flask with a yellowish substance.")
        print("'Drink this and try to sleep,'")
        print("'we'll see each other again at some point'")
        print("She gives you a warm smile and leaves the room.")
        print("You wake up but have no idea how much time has passed.")
        print("The room decor looks different.")
        print("You look at the calendar.")
        print("1962; Great the drink worked")
        print("You get up and walk down to the only place you haven't")
        print("explored yet: the basement")
        print("The dark room appears to have")
        print("a large metal construction")
        print("Quite odd for something in a household")
        print("The giant metal box has an entrance")
        print("and two levers inside")
        blue_or_red()

    elif response in [CARRY_ON, CARRY_ON.capitalize()]:
        print("You walk along the corridor")
        print("and you suddenly hear knocking at the front door.")
        open_or_not()


def blue_or_red():
    '''
    Function allows user to decide whether they will pick the RED or BLUE
    option. Called by open_or_carry_on() function.
    '''
    print("One is red, the other blue. What's your pick?")
    print("blue/red")
    response = input("")
    print("")
    print("")
    print("")
    print("")
    while response not in [BLUE, RED, BLUE.capitalize(), RED.capitalize()]:
        print("Invalid response, please try again")
        response = input("")

    if response in [RED, RED.capitalize()]:
        # This is an empty line pause before the next piece of text is printed.
        print("")
        # The user's response is confirmed here.
        print(f"You picked {response}")
        print("You have been sucked into a black hole.")
        print("")
        print("The time capsule couldn't take the pressure")
        print("")
        print("Game over.")
        print("")
        print("")
        quit()
    elif response in [BLUE, BLUE.capitalize()]:
        print(f"You picked {response}")
        print("You feel the machine shaking and tumbling around.")
        print("You wake up in the woods. The ones next to your home.")
        print("It's impossble to tell what year it is")
        print("So you leave the time machine in the woods")
        print("and head to the house")
        print("As you enter everything looks familiar.")
        print("Your mum walks in from the living room")
        print(f"'Hi, {NAME}, how was school?'")
        print("You made your way home, congratulations!")
        quit()


def open_or_not():
    '''
    The user can decide whether to open the door or not in the game.
    This function uses the "ANSWER" and "IGNORE" keywords.
    Called by the open_or_carry_on() function.
    '''
    print("Will you open the door? (answer/ignore)")
    response = input("")
    print("")
    print("")
    print("")
    print("")

    while response not in [ANSWER, IGNORE, ANSWER.capitalize(),
                           IGNORE.capitalize()]:
        print("Invalid response, please try again.")
        response = input("")
    if response in [ANSWER, ANSWER.capitalize()]:
        print("You walk down the stairs and towards the front door")
        print("You open the door and see no one.")
        print("Instead of a person you spot a parcel")
        print("on the ground.")
        print("You see your name written in beautiful,")
        print("cursive handwriting on the brown wrapping paper.")
        print("Upon opening the package you realise")
        print("it held a watch. It has a golden crown on the side")
        spin_up_or_down()
    elif response in [IGNORE, IGNORE.capitalize()]:
        print("You head to the garden")
        print("and spot a large shed in the corner")
        print("When entering you notice a huge metal construction")
        print("You also spot it has an entrance")
        print("You step inside and find two different")
        print("coloured levers")
        blue_or_red()


def spin_up_or_down():
    '''
    This function operates through the "UP" and "DOWN" keywords. It is
    called by the open_or_not() function.
    '''
    print("Do you want to spin the crown up or down?")
    response = input("")
    print("")
    print("")
    print("")
    print("")

    while response not in [UP, DOWN, UP.capitalize(), DOWN.capitalize()]:
        print("Invalid response, please try again.")
        response = input("")
    if response in [UP, UP.capitalize()]:
        print("You spin upwards.")
        print("Your surroundings become blurred.")
        print("You start to sway and realise")
        print("you can no longer hold yourself up.")
        print("Your vision goes fully black.")
        print("...")
        print("")
        print("")
        print("When you open your eyes you recognise your home;")
        print("However when you look down at the watch")
        print("it is smashed, rusty and looks nothing like")
        print("it did in the 1920s from which you came.")
        print("You made it back, congratulations")
        quit()
    elif response in [DOWN, DOWN.capitalize()]:
        print("You spin down.")
        print("Your surroundings become blurred.")
        print("You start to sway and realise")
        print("you can no longer hold yourself up.")
        print("Your vision turns fully black.")
        print("...")
        print("")
        print("")
        print("When you open your eyes you are still lying down")
        print("in the hallway")
        print("The bright green wallpaper draws your attention")
        print("as it's different from the previous 1920 decor")
        print("You check the newspaper on top of the")
        print("large table on the side.")
        print("23.06.1962")
        print("You wonder who dropped the watch off")
        print("at the front door. They must have known you.")
        leave_or_explore()


def leave_or_explore():
    '''
    Function allows user to pick between LEAVE/EXPLORE keywords.
    Called by the spin_up_or_down() function
    '''
    print("Do you wish to leave the house or explore the house?\n")
    print("(leave/explore)")
    response = input("")
    print("")
    print("")
    print("")
    print("")

    while response not in [LEAVE, EXPLORE, LEAVE.capitalize(),
                           EXPLORE.capitalize()]:
        print("Invalid response, please try again")
        response = input("")
    if response in [LEAVE, LEAVE.capitalize()]:
        print("You step outside")
        print("The house is in the countryside")
        print("surrounded by woodlands")
        print("As you walk further out you spot a silhouette")
        print("standing next to a tree")
        print("You try to ignore it and keep walking")
        print("You are now very far from your front door")
        print("The figure starts walking towards you")
        print("")
        print("He's running.")
        print("He runs up to you.")
        print('"I need that watch" says the man')
        print("He looks very impatient")
        print("Something doesn't feel right and")
        print("You begin to run")
        print("At this point the closest house is the ")
        print("neighbours house.")
        print("Your sprint to the front door")
        print("And frantically pound on the front door")
        print("A tall man opens the door")
        print("He glances at you and then")
        print("at the watch you're holding")
        print("He looks past you and sees the figure behind you")
        print("You read fear and distress from his face")
        print("He pushes you inside and slams the door shut")
        print(f"You must be {NAME}, I was told you would")
        print("be coming")
        print("He takes the broken watch and inspects it")
        print("We'll have to fix that if you want to return home")
        print("He walks into a small cluttered room and begins")
        print("to fix the smashed watch")
        print("A few minutes lates he hands you the watch")
        print("and instructs that you spin upwards")
        print("You follow the instructions and your vision ")
        print("becomes blurry again.")
        print("You have escaped back to your time, congratulations")
        quit()
    if response in [EXPLORE, EXPLORE.capitalize()]:
        explore_house()


def explore_house():
    '''
    Function calls number_verification() function so the player can input
    as many number combinations as they want until they are happy with the
    outcome. It is called by leave_or_explore().
    '''
    print("You wonder off into the attic")
    print("Amongst all the clutter you spot")
    print("a wooden door; about a metre tall.")
    print("It's locked with a heavy padlock.")
    print("The current combinaton reads")
    print("1")
    print("9")
    print("6")
    print("2")
    print("Try and set the lock to your year")
    number_verification()


def verify_user_response():
    '''
    The function verifies if the user is happy with their response for the
    year combination. It calls number_verification() if the user chooses
    no as the answer. Otherwise the game ends.
    '''
    print("Is that the correct year? (yes/no)")
    response = input("")
    while response not in [YES, NO, YES.capitalize(), NO.capitalize()]:
        print("Invalid response, please try again")
        response = input("")
    if response in [YES, YES.capitalize()]:
        print("Congratulations, you completed the game")
        quit()
    if response in [NO, NO.capitalize()]:
        print("Try typing in the combination again")
        number_verification()


def number_verification():
    '''
    Checks if the user's response is an integer. If not the user must
    input the number again. Function called by explore_house().
    Function repeats itself if user input is not a number.
    '''
    try:
        response = int(input(""))
        print(f"You have chosen {response}")
        verify_user_response()
    except ValueError:
        # If input is not an integer this is considered an error.
        print("That was not a number. Try again...")
        number_verification()


def main():
    '''
    This function runs the game by calling begin_game()
    '''
    begin_game()


if __name__ == '__main__':
    main()
