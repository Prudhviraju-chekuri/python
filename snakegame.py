import tkinter as tk
import random

# Game settings
WIDTH = 600
HEIGHT = 400
SQUARE_SIZE = 20
DELAY = 100  # milliseconds

# Colors
BG_COLOR = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()

        self.restart_button = tk.Button(root, text="Restart Game", font=("Arial", 14),
                                        command=self.restart_game, state=tk.DISABLED)
        self.restart_button.pack(pady=10)

        self.root.bind("<KeyPress>", self.change_direction)

        self.reset_game()
        self.update()

    def reset_game(self):
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = 'Right'
        self.running = True
        self.food = None
        self.spawn_food()
        self.restart_button.config(state=tk.DISABLED)
        self.canvas.delete("all")

    def restart_game(self):
        self.reset_game()
        self.update()

    def spawn_food(self):
        while True:
            x = random.randint(0, (WIDTH - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE
            y = random.randint(0, (HEIGHT - SQUARE_SIZE) // SQUARE_SIZE) * SQUARE_SIZE
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def change_direction(self, event):
        key = event.keysym
        opposite = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
        if key in opposite and key != opposite.get(self.direction):
            self.direction = key

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            head_y -= SQUARE_SIZE
        elif self.direction == 'Down':
            head_y += SQUARE_SIZE
        elif self.direction == 'Left':
            head_x -= SQUARE_SIZE
        elif self.direction == 'Right':
            head_x += SQUARE_SIZE

        # Wrap-around logic
        head_x %= WIDTH
        head_y %= HEIGHT

        new_head = (head_x, head_y)

        # End game if snake hits itself
        if new_head in self.snake:
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.spawn_food()
        else:
            self.snake.pop()

    def draw_elements(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill=SNAKE_COLOR)
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx + SQUARE_SIZE, fy + SQUARE_SIZE, fill=FOOD_COLOR)

    def update(self):
        if self.running:
            self.move_snake()
            self.draw_elements()
            self.root.after(DELAY, self.update)
        else:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over", fill="white", font=("Arial", 24))
            self.restart_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
