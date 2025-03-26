import random
import tkinter as tk

# Constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 300
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.squares = []
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        self.coordinates = [
            random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE,
            random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        ]
        canvas.create_oval(
            self.coordinates[0], self.coordinates[1],
            self.coordinates[0] + SPACE_SIZE, self.coordinates[1] + SPACE_SIZE,
            fill=FOOD_COLOR, tag="food"
        )

def next_turn(snake, food):
    global direction  

    # Get current head position
    x, y = snake.coordinates[0]
    
    # Move in the current direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Insert new head position
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
    snake.squares.insert(0, square)
    
    # Check if food is eaten
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()  # Create new food
    else:
        # Remove last part of snake to keep it moving
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    # Check collisions
    if check_collisions(snake):
        game_over()
        return

    # Schedule next movement
    window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Check if snake hits the wall
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    
    # Check if snake collides with itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False

def game_over():
    canvas.delete("all")
    canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")

# Initialize Tkinter window
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

# UI Elements
label = tk.Label(window, text=f"Score: {score}", font=('consolas', 40))
label.pack()

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Center window on screen
window.update_idletasks()  # Ensure correct widget dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Key bindings for movement
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Start game
snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
