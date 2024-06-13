import random

class Task4:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.userScore = 0
        self.computerScore = 0

    def userChoice(self):
        while True:
            userChoice = input("rock, paper, scissors: ").lower()
            if userChoice in self.choices:
                return userChoice
            else:
                print("not valid, try again")

    def computerChoice(self):
        return random.choice(self.choices)

    def winner(self, userChoice, computerChoice):
        if userChoice == computerChoice:
            return "tie"
        elif (userChoice == "rock" and computerChoice == "scissors") or (userChoice == "scissors" and computerChoice == "paper") or (userChoice == "paper" and computerChoice == "rock"):
            return "user"
        else:
            return "computer"

    def resultDisplay(self, userChoice, computerChoice, winner):
        print(f"user's choice: {userChoice.capitalize()}")
        print(f"computer's choice: {computerChoice.capitalize()}")
        if winner == "tie":
            print("it is a tie")
        elif winner == "user":
            print("you are winner")
        else:
            print("you lost")

    def playAgain(self):
        while True:
            again = input("do you want to play again? (yes/no): ").lower()
            if again == "yes":
                return True
            elif again == "no":
                return False
            else:
                print("invalid input, please enter 'yes' or 'no': ")

    def gamePlay(self):
        while True:
            userChoice = self.userChoice()
            computerChoice = self.computerChoice()
            winner = self.winner(userChoice, computerChoice)
            self.resultDisplay(userChoice, computerChoice, winner)
            
            if winner == "user":
                self.userScore += 1
            elif winner == "computer":
                self.computerScore += 1

            print(f"user's score: {self.userScore}")
            print(f"computer's score: {self.computerScore}")

            if not self.playAgain():
                break

if __name__ == "__main__":
    game = Task4()
    game.gamePlay()
