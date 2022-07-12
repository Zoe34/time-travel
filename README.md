# Time Travel
The Time Travel Game runs on Heroku and is a terminal game.
It is a choice based game, where the player's input determines what happens


## How to play
The user must read the text as it appears on the screen and choose between two options provided.
The game has several choices, which determine how the game would end.
One of the first questions asked is "What's your name?", which is later fed back in the game when referring to the player.
The aim is to time travel to the future, as the game begins in 1920.
The player must try to pick the right choices to move back to the current year.
When the player manages to return to the present moment a congratulating message appears.
Some outcomes lead to a "Game over" message if the player lost.
After winning and losing the game automatically restarts.
## Features
There is one main page from which the game operates and allows the user to submit their responses

### Existing features
Questions for the player and a selection of answers they can choose:

Sometimes the game confirms the choices made by the user by feeding back the answer:

If the player inputs an answer that isn't within the list of options a message appears:

During the game lines of text appear, telling a story. The output depends on the choices the player makes throughout the game:

When the player loses the game or decides they no longer want to play the game is reset and a goodbye message appears:


### Future Features
More options within the game to make it slightly longer.


## Data model
The game is based on a story which unfolds. The direction and outcome depend on the user's choice e.g., "answer/ignore".
The text of the story is printed using "print_text" and the player is referred to by their name in the game using an f string: print_text(f"Hi {name}!", 2)
The 2 after every line of text is the amount of time delayed between each printed line.

## Testing
The game has been tested using PEP8 linter and returned no problems.
### Bugs
### Remaining bugs
### Validator testing

## Deployment

## Credits