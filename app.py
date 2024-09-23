from tkinter import *
import random

# Constants defining game window size, speed, space size, and colors
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 120  # Speed of the game (time delay in milliseconds between moves)
SPACE_SIZE = 20  # Size of each square (both for snake and food)
BODY_PARTS = 3  # Initial number of snake body parts
SNAKE_COLOR = "#00FF00"  # Green color for snake
FOOD_COLOR = "#FF0000"  # Red color for food
BACKGROUND_COLOR = "#000000"  # Black background

# Snake class manages snake attributes and behavior
class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS  # Initialize snake with predefined body size
        self.coordinates = []  # List to store snake's body coordinates
        self.squares = []  # List to store snake's body parts (rectangles)

        # Initialize the snake's body at the top-left corner (0,0)
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Draw snake on canvas based on its coordinates
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Food class to create and manage the food position on the canvas
class Food:

    def __init__(self):
        # Randomly place food on the grid within the game area
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]  # Store food coordinates

        # Draw the food as a red circle (oval) on the canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Function to handle each "turn" or movement of the snake
def next_turn(snake, food):

    x, y = snake.coordinates[0]  # Get the head of the snake (first element of coordinates list)

    # Determine new position of the snake's head based on the direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Insert new head position at the beginning of the coordinates list
    snake.coordinates.insert(0, (x, y))

    # Create new rectangle for the head at the new position
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)  # Add it to the snake's list of squares

    # Check if the snake eats the food (head coordinates match food coordinates)
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score  # Access global score variable
        score += 1  # Increment the score

        # Update the score label
        label.config(text="Score:{}".format(score))

        # Remove current food and generate a new one
        canvas.delete("food")
        food = Food()

    else:
        # If no food is eaten, remove the last part of the snake's body
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Check for collisions with walls or itself
    if check_collisions(snake):
        game_over()  # End the game if there's a collision
    else:
        # Continue the game by calling next_turn after a delay (based on SPEED)
        window.after(SPEED, next_turn, snake, food)

# Function to change the direction of the snake based on user input
def change_direction(new_direction):

    global direction  # Access global direction variable

    # Prevent the snake from reversing direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

# Function to check if the snake collides with walls or itself
def check_collisions(snake):

    x, y = snake.coordinates[0]  # Get the head position

    # Check if the head hits the walls
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    # Check if the head collides with the body
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Function to handle game over scenario
def game_over():
    canvas.delete(ALL)  # Clear the canvas
    # Display "GAME OVER" message in the middle of the canvas
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

# Setting up the game window
window = Tk()
window.title("Snake game")
window.resizable(False, False)  # Disable window resizing

score = 0  # Initial score
direction = 'down'  # Initial direction of the snake

# Label to display score
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# Canvas to display the game elements (snake, food, etc.)
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Calculate the window's position on the screen to center it
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

# Set the window's geometry (size and position)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind arrow keys to change direction
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Initialize the snake and food objects
snake = Snake()
food = Food()

# Start the first turn of the game
next_turn(snake, food)

# Run the Tkinter main loop
window.mainloop()
