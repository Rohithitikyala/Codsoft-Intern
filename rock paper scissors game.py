import tkinter as tk
import random

def play():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    player_choice = player_var.get()
    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer's choice: {computer_choice}\n{result}")

root = tk.Tk()
font=("sans-serif aerial",18,"italic")
root.title("Rock Paper Scissors")
player_var = tk.StringVar()
tk.Label(root, text="Choose Rock, Paper, or Scissors:",font=("times new roman",24,"bold")).pack()
tk.Radiobutton(root, text="Rock", variable=player_var, value="Rock",font=font).pack(anchor=tk.W)
tk.Radiobutton(root, text="Paper", variable=player_var, value="Paper",font=font).pack(anchor=tk.W)
tk.Radiobutton(root, text="Scissors", variable=player_var, value="Scissors",font=font).pack(anchor=tk.W)

play_button = tk.Button(root, text="Play", command=play,font=font)
play_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
