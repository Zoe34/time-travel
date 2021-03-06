# Time Travel
The Time Travel Game runs on Heroku and is a terminal game.
It is a choice based game, where the player's input determines what happens.
The link to the game can be found here: https://time-travel22.herokuapp.com/


## How to play
The user must read the text as it appears on the screen and choose between two options provided.
The game has several choices, which determine how the game would end.
One of the first questions asked is "What's your name?", which is later fed back in the game when referring to the player.
The aim is to time travel to the future, as the game begins in 1920.
The player must try to pick the right choices to move back to the current year.
When the player manages to return to the present moment a congratulating message appears.
Some outcomes lead to a "Game over" message if the player lost.
After winning or losing the game stops.
To refresh the game the player needs to click "RUN PROGRAM"

## Features

### Existing features
Questions for the player and a selection of answers they can choose:
![Question for the player](assets/game-screenshots.png/answers.png)

Sometimes the game confirms the choices made by the user by feeding back the answer:
![Answer confirmation](assets/game-screenshots.png/confirmation.png)


If the player inputs an answer that isn't within the list of options a message appears:
![Invalid response message](assets/game-screenshots.png/invalid-response.png)


During the game lines of text appear, telling a story. The output depends on the choices the player makes throughout the game:
![Outcome of player's decision](assets/game-screenshots.png/outcome-one.png)
![Outcome of player's decision](assets/game-screenshots.png/outcome-two.png)



When the player loses the game a message appears:
![Message when player loses](assets/game-screenshots.png/game-lost.png)

When the player wins the game a message appears:
![Message when player wins](assets/game-screenshots.png/game-won.png)

When the player decides they no longer want to play this message appears:
![Message when player quits](assets/game-screenshots.png/game-quit.png)


### Future Features
- More options within the game to make it slightly longer.
- A score/point count


## Data model
- The game is based on a story which unfolds. The direction and outcome depend on the user's choice e.g., "answer/ignore".
- The text of the story is printed using "print_text" and the player is referred to by their name in the game using an f string: print_text(f"Hi {NAME}!", 2)
- The flowchart for this game was created using Lucidchart:
![Flowchart image](assets/flowchart.png)

## Testing

### Bugs
The bugs I came across with pylint:
1. ms-toolsai.jupyter extension is not synced, but not added in .gitpod.yml:
Fixed by clicking on the options in Quick Fixes for .gitpod.yml
2. Constant name "name" doesn't conform to UPPER_CASE naming stylepylint(invalid-name):
Fixed by changing "name" to "NAME" on line 50, 51 and within the rest of the code.
3. Using the global statementpylint(global-statement):
The third bug was fixed by moving 'NAME' to the keywords file and adding it to the imported keywords list in run.py.

### Remaining bugs
All bugs have been fixed.

### User stories:
- As a new user I would like to operate using simple words and make decisions within the game:
![Question screenshot](assets/game-screenshots.png/decisions.png)

- I would like to quickly understand how the game works when starting it:
![Explanation of the game](assets/game-screenshots.png/explanation.png)
- I would like to receive confirmation of my choices whenever I decide about the course of the game:
![Confirmation of choices](assets/game-screenshots.png/confirmation.png)
- I would like to play the game in the form of an interactive story, which contains a timeline and a plot:
![Main storyline](assets/game-screenshots.png/storyline.png)
- As a new user I would like to get a message if I write the incorrect answer by mistake:
![error message](assets/game-screenshots.png/error-message.png)


### Validator testing
The game has been tested using PEP8 Python Validator and returned no problems.

## Technology:
- Heroku was used to deploy this project and create the live link
- The project was made in Gitpod, and any commits were pushed to the repository in GitHub.
- Lucidchart was used to create the flowchart for this project as a baseline plot for the game.
- The PEP8 Python Validator Test was used to check for any errors.
- Python linting was used to check for any problems during the development of the game.

## Deployment
The repository was created in GitHub using "New" on the right - hand side in the repository section.
The template was provided by Code Institute: https://github.com/Code-Institute-Org/python-essentials-template

### GitHub:
To open the code for this project through GitHub enter https://github.com/Zoe34/time-travel.git into the browser.
Click the green "Gitpod" button.
Click "cancel" and then "More actions"; "Open in browser"

### Deploying to Heroku:
- New App clicked in the top right-hand corner of Heroku
- The app was named time-travel22
- The location was set to Europe before the app was created
- The python and node.js buildpacks were added and saved
- In the Deploy section the deployment was connected to GitHub
- The repository was searched by name and connected to Heroku
- The project was manually deployed
- Once the project has been deployed "View" was clicked to open the deployed app.

## Credits
- Code Institute has provided the template for this project.
- The flowchart for this game was made using Lucidchart
- Stackoverflow was used for guidance and help when creating this project.
