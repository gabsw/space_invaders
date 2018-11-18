# SPACE INVADERS GAME
Space invaders is an iconic arcade game. The game has been implemented based on the tutorial found in “Python Crash Course”, using pygame. To run the game, you will have to download the files to your IDE and run the ```run_game.py``` file. This will be fixed in the future`, for a smoother user experience.

##Design
The implementation has been structured using the following classes:

* Alien: models the behavior of a fleet of aliens.

* Bullet: models the behavior of a group of bullets.

* Button: creates the “Play” button to start the game.

* Functions: contains the functions that change the state of the game.

* GameStats: tracks statistics such as level, scores and lives left.

* Scoreboard: displays rendered images of the levels, score, high score and lives left.

* Settings: defines the graphical aspects of the game and movement of the game objects.

* Ship: models the behavior of a single ship that will be controlled by the player.

The gameplay sequence of the game is coded on the file ```run_game.py```. 

##Rules
Your goal is to shoot down as many aliens as you can, without your ship being hit. You will have 3 lives to achieve the highest score that you can before the game is over. You can use your arrow keys to move your ship left and right and space bar to shoot bullets. Your ammunition is infinite, but you can only shoot 3 bullets at a time. If you manage to shoot down the whole fleet, a new level will start, where the aliens will move faster.
