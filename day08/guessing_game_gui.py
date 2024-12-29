import tkinter as tk
from tkinter import messagebox
import random

def game_logic(guess, target):
    """Handles the game logic, returning a message."""
    if guess == target:
        return "Guess was exact! You win!"
    elif guess < target:
        return "Guess is too small"
    else:
        return "Guess is too big"

def start_game():
    global target  # Use global to modify the target
    target = random.randint(1, 20)
    output_label.config(text="Starting new game:")
    guess_entry.config(state=tk.NORMAL)  # Enable entry field
    guess_button.config(state=tk.NORMAL)
    cheat_button.config(state=tk.NORMAL)
    new_game_button.config(state=tk.DISABLED)


def check_guess():
    try:
        user_guess = int(guess_entry.get())
        result = game_logic(user_guess, target)
        output_label.config(text=result)
        if result == "Guess was exact! You win!":
            guess_entry.config(state=tk.DISABLED) # Disable entry field
            guess_button.config(state=tk.DISABLED)
            cheat_button.config(state=tk.DISABLED)
            new_game_button.config(state=tk.NORMAL)
            
        guess_entry.delete(0, tk.END)  # Clear the entry field
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")
        guess_entry.delete(0, tk.END)

def cheat():
    output_label.config(text=f"Cheater! The number is: {target}")

def exit_game():
    root.destroy()

root = tk.Tk()
root.title("Guessing Game")

# Widgets
output_label = tk.Label(root, text="Welcome!")
guess_label = tk.Label(root, text="Enter your guess (1-20):")
guess_entry = tk.Entry(root, state=tk.DISABLED)
guess_button = tk.Button(root, text="Submit Guess", command=check_guess, state=tk.DISABLED)
cheat_button = tk.Button(root, text="Cheat", command=cheat, state=tk.DISABLED)
new_game_button = tk.Button(root, text="New Game", command=start_game)
exit_button = tk.Button(root, text="Exit", command=exit_game)

# Layout (using grid)
output_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
guess_label.grid(row=1, column=0, padx=5, pady=5)
guess_entry.grid(row=1, column=1, padx=5, pady=5)
guess_button.grid(row=1, column=2, padx=5, pady=5)
cheat_button.grid(row=2, column=1, padx=5, pady=5)
new_game_button.grid(row=3, column=1, padx=5, pady=5)
exit_button.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()