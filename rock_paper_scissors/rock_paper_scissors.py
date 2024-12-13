import tkinter as tk
from tkinter import PhotoImage, Button, Label
import random

class GameApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Rock Paper Scissors")  # Title bar customisation
		self.root.geometry("527x472")           # Adjust as needed
		self.root.resizable(False,False)        # Window is not resizable
		self.root.config(bg='#262626')          # Color of the window

		# Initialize game state
		self.player_score = 0
		self.computer_score = 0

		# Label for player score
		self.label_player = tk.Label(root, text=f"Player Score: {self.player_score}", font=("Terminal", 14)
		                             ,bg='#262626',fg="white")
		# *Placing label for player score
		self.label_player.grid(row=0, column=0, padx=10, pady=10, sticky="w")

		# Reset button
		self.reset_button = Button(root,text="Reset", font=("Terminal",10),
		                           bg='#262626',fg="white",command=self.reset_game)
		# *Placing reset button
		self.reset_button.grid(row=0, column=1,  columnspan=1, padx=10, pady=10, sticky="we")

		# Label for computer score
		self.label_computer = tk.Label(root, text=f"Computer Score: {self.computer_score}", font=("Terminal", 14)
		                               ,bg='#262626',fg="white")
		# *Placing label for computer score
		self.label_computer.grid(row=0, column=2, padx=10, pady=10, sticky="e")

		# Load images
		self.rock_img = PhotoImage(file="rock.png")
		self.paper_img = PhotoImage(file="paper.png")
		self.scissors_img = PhotoImage(file="scissors.png")

		# Creating a dictionary for mapping images
		self.choice_images = {
			"rock": self.rock_img,
			"paper": self.paper_img,
			"scissors": self.scissors_img
		}

		# Button images
		self.rock_button_img = PhotoImage(file="rock_button.png")
		self.paper_button_img = PhotoImage(file="paper_button.png")
		self.scissor_button_img = PhotoImage(file="scissors_button.png")


		# Image display for player choice
		self.image_player = tk.Label(root, image=random.choice([self.rock_img,self.paper_img,self.scissors_img]),
		                             width=200, height=215,bg="#262626") # when the game begins is random image
		# *Placing the image for player choice                            # then it's updated with every button click
		self.image_player.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky="w")

		# Versus label between images
		self.image_label_versus = tk.Label(root, text="VS", font=("Terminal", 30),
		                                   bg='#262626',fg="white")
		self.image_label_versus.grid(row=1,column=1,columnspan=1,padx=0,pady=5)

		# Image display for computer choice
		self.image_computer = tk.Label(root, image=random.choice([self.rock_img,self.paper_img,self.scissors_img]),
		                               width=200, height=215,bg="#262626") # when the game begins is random image then
		# *Placing the image for computer choice                            # it's updated with the computer's random choice
		self.image_computer.grid(row=1, column=2, columnspan=1, padx=5, pady=5, sticky="e")

		# Label for winner confirmation
		self.winner_label = Label(root,font=("Terminal",20),bg="#262626")
		# *Placing winner label
		self.winner_label.grid(row=2,column=0,columnspan=3,sticky="we")

		# Rock button  # Player choice button
		self.rock_button = Button(root,image=self.rock_button_img,width=80, height=96,bg="#262626",
		                          command= lambda: self.player_choice('rock')) # player choice becomes 'rock'
		# *Placing rock button                                                  # after pressing button
		self.rock_button.grid(row=3, column=0, columnspan=1, padx=5, pady=10, sticky="e")

		# Paper button  # Player choice button
		self.paper_button = Button(root,image=self.paper_button_img,width=83, height=115,bg="#262626",
		                           command=lambda: self.player_choice('paper')) # player choice becomes 'paper'
		# *Placing paper button                                                  # after pressing button
		self.paper_button.grid(row=3, column=1,  columnspan=1, padx=5, pady=10)

		# Scissors button  # Player choice button
		self.scissors_button = Button(root,image=self.scissor_button_img,width=80, height=115,bg="#262626",
		                              command=lambda: self.player_choice('scissors')) # player choice becomes 'scissors'
		# *Placing scissors button                                                     # after pressing button
		self.scissors_button.grid(row=3, column=2,  columnspan=1, padx=5, pady=10, sticky="w")

		# Status label
		self.status_label = Label(root,text="Pick!", font=("Terminal",20),bg="black",fg="white")
		# *Placing status label
		self.status_label.grid(row=4, column=0, columnspan=3,sticky="we")

	# Function for computer choice
	def computer_choice(self):
		computer_choice = random.choice(['rock', 'paper', 'scissors']) # List of choices for computer
		return computer_choice # Computer choice is from the list identical to what player choice buttons return

	# Function for player choice
	def player_choice(self,choice):
		# Call computer_choice to get the computer's choice
		computer_choice = self.computer_choice() # Creating variable for return value from computer_choice function

		# Changing the image to player's choice
		self.image_player.config(image=self.choice_images[choice]) # Line 38 in code

		# Call determine_winner to compare the choices and update the scores
		self.determine_winner(choice, computer_choice) # determine_winner is the function bellow

	def determine_winner(self, player_choice, computer_choice):
		# Display image for computer's choice
		self.image_computer.config(image=self.choice_images[computer_choice])

		# Check if it's a draw
		if player_choice == computer_choice:
			# The score will be unchanged but confirming with both labels the draw
			self.status_label.config(text="Draw!",bg="#ccbb00",fg="black")
			self.winner_label.config(text="Draw!",bg="#ccbb00",fg="black")
			return "draw"

		# Check if player wins
		if (player_choice == 'rock' and computer_choice == 'scissors') or \
				(player_choice == 'scissors' and computer_choice == 'paper') or \
				(player_choice == 'paper' and computer_choice == 'rock'):
			self.status_label.config(text=f"{player_choice.title()} beats {computer_choice.title()}",
			                         bg="#006655",fg="white") # Label for ex. paper beats rock
			self.winner_label.config(text="Player wins!",bg="#006655",fg="white") # Updating label with winner
			self.player_score += 1  # Increment player score
			self.label_player.config(text=f"Player Score: {self.player_score}") # Updating score label
			return "player"

		# If the computer wins
		self.status_label.config(text=f"{computer_choice.title()} beats {player_choice.title()}",
		                         bg="#b00b00",fg="white") # Label for ex. paper beats rock
		self.winner_label.config(text="Computer wins!",bg="#b00b00",fg="white") # Updating label with winner
		self.computer_score += 1  # Increment computer score
		self.label_computer.config(text=f"Computer Score: {self.computer_score}") # Updating score label
		return "computer"

	def reset_game(self):
		self.player_score = 0   # Resetting score variable
		self.computer_score = 0 # Resetting score variable
		self.status_label.config(text="Pick!",bg="black",fg="white") # Resetting the label
		self.label_player.config(text=f"Player Score: {self.player_score}")       # Updating label with score 0
		self.label_computer.config(text=f"Computer Score: {self.computer_score}") # Updating label with score 0
		self.winner_label.config(text="",bg="#262626") # Resetting the label


# Main loop
if __name__ == "__main__":
	root = tk.Tk()
	app = GameApp(root)
	root.mainloop()
