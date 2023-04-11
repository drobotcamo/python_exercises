print("Welcome to rock paper scissors ULTIMATE\n")
p1Selection = input("Player 1, please enter your selection: \n").lower()
p2Selection = input("Player 2, please enter your selection: \n").lower()

selection = ["rock", "paper", "scissors"]
result = ""
if selection.index(p1Selection) != len(selection):
    winningOption = selection[selection.index(p1Selection) + 1]
else:
    winningOption = selection[0]
if winningOption == p2Selection:
    result = "Player 2 Victory"
elif p1Selection == p2Selection:
    result = "Tie"
else:
    result = "Player 1 Victory"


print(f"Congratulations! The result is a resounding {result}")