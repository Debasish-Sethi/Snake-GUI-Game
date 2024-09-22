# Snake Game - Python (Tkinter)

Welcome to the Snake Game, a classic arcade game built using Python and Tkinter. This game is simple yet engaging, where you control a snake to eat food and grow, while avoiding collisions with the walls or yourself. The objective is to eat as much food as possible, increasing your score, while keeping the snake alive.

# Features
* **Snake Growth**: Every time the snake eats food, it grows in size, and the score increases.
* **Random Food Placement**: Food appears randomly on the grid within the game window.
* **Game Over**: The game ends when the snake collides with the walls or itself.
* **Score Tracking**: The current score is displayed at the top of the window.
* **Responsive Keyboard Controls**: Control the snake using arrow keys (↑, ↓, ←, →).

# Getting Started

### Prerequisites
Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/)

No external libraries are required beyond the standard Python `tkinter` library, which comes pre-installed with most Python distributions.

### How to Run
1. Clone this repository to your local machine using:
``` bash
git clone https://github.com/your-username/snake-game.git
```
2. Navigate to the project directory:
``` bash
cd snake-game
```
3. Run the Python script:
```bash
python snake_game.py
```
### Controls
* **Arrow Keys**: Use the arrow keys on your keyboard to change the direction of the snake.
### Game Rules
* **Move the Snake**: The snake automatically moves in the current direction every turn.
* **Eat the Food**: Navigate the snake towards the red food to eat it.
* **Grow**: Each time the snake eats food, its length increases.
* **Avoid Collisions**: The game ends if the snake hits the walls or itself.

### Screenshots
* **Game Start**  
(Screenshot of the game in the initial state with a short snake and a food item)
* **Game Over**  
(Screenshot of the game over screen when the snake collides with a wall or itself)

# Code Overview
### Main Components
* **Snake Class**: Manages the snake's body, movement, and behavior.
* **Food Class**: Handles food creation and placement.
### Main Functions
1. `next_turn(snake, food)`: Manages the snake's movement, food consumption, and collision checks.
2. `change_direction(new_direction)`: Updates the snake's direction based on user input.
3. `check_collisions(snake)`: Checks if the snake has collided with the wall or itself.
4. `game_over()`: Displays a game-over message and stops the game.
### Constants
* `GAME_WIDTH`, `GAME_HEIGHT`: Define the size of the game window.
* `SPEED`: Controls the speed of the game (milliseconds per move).
* `SPACE_SIZE`: The size of each square that makes up the snake and food.
* `BODY_PARTS`: The initial number of snake segments.
* `SNAKE_COLOR`, `FOOD_COLOR`, `BACKGROUND_COLOR`: Define the colors of the snake, food, and background.

### Future Improvements
* **Difficulty Levels**: Add different speed levels based on the player's score.
* **High Score Feature**: Implement a high score tracking system.
* **Pause/Resume Functionality**: Allow the player to pause and resume the game.
* **Enhanced Graphics**: Introduce a more modern or retro style for the snake and food.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contribution
Feel free to fork this repository, make improvements, and submit a pull request. All contributions are welcome!
