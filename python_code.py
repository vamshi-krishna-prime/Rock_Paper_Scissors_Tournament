# """This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""
# """The Player class is the parent class for all of the Players"""

import random

moves = ['rock', 'paper', 'scissors']


# Parent class
class Player:
    def move(self):
        return RandomPlayer.random_move(self)

    # Learn function to memorize opponent's move and return the same
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return self.their_move


# Human class which allows the users to play the game
class HumanPlayer(Player):
    def move(self):
        return input("rock, paper, scissors ? > ").lower()


# Reflect class which mimics the opponent's move in the next round
class ReflectPlayer(Player):
    def __init__(self):
        self.round = 0

    def move(self):
        # Since it cannot mimic opponent's move in the first Round
        # It returns a random move from the moves list
        while self.round == 0:
            self.round += 1
            return RandomPlayer.random_move(self)
        # returns the opponent's move from the previous round
        return self.their_move


# CyclePlayer class which cycles its own moves from the 'moves' list
class CyclePlayer(Player):
    def __init__(self):
        self.round = 0

    def move(self):
        # Round 1 returns a random move
        while self.round == 0:
            self.round += 1
            return RandomPlayer.random_move(self)
        # Round 2 returns the adjacent/next item from the 'moves' list
        try:
            return moves[moves.index(self.my_move) + 1]
        # If index exceeds the length of the list,
        # It circles back to its fist item
        except IndexError:
            return moves[0]


# RandomPlayer class which returns a random move from the 'moves' list
class RandomPlayer(Player):
    def random_move(self):
        return random.choice(["rock", "paper", "scissors"])


# Constant player class which returns a constant - 'rock'
class ConstantPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# beats function which returns a boollean vaule of game rule
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Game class which decides the length of the game, announce winner
# and condition to terminate the game
class Game():
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p1.name = "Player 1"
        self.p2.name = "Player 2"
        self.p3.name = "Player 3"
        self.p4.name = "Player 4"
        self.p1.win = 0
        self.p2.win = 0
        self.p3.win = 0
        self.p4.win = 0
        self.round = 0
        self.game = "initialized"
        # self.sub_round_one.winner = 0
        # self.sub_round_two.winner = 0
        self.winner = " "

    # function to announce the winner scenario
    def announce_winner(self):
        print(f"\nTotal Score : "
              f"Opponent Wins - {self.p1.win}, Your Wins - {self.p2.win}")
        if self.p1.win > self.p2.win:
            print("Game Result : ** Opponent wins the Game **")
        elif self.p1.win < self.p2.win:
            print("Game Result : ** You win the Game **")
        else:
            print("Game Result : ** The Game is a Tie **")

    def play_round(self):
        self.winner1 = self.play_sub_round(self.p1, self.p2)
        self.winner2 = self.play_sub_round(self.p3, self.p4)
        self.play_sub_round(self.winner1, self.winner2)


    def play_sub_round(self, c1, c2):
        move1 = c1.move()
        # calls the player2 move
        move2 = c2.move()
        # In case user injects a unrecognized input, it loops itself
        while move1 not in moves:
            move1 = c1.move()
        print(f"{c1.name} played\t: {move1}  \n{c2.name} Played : {move2}")
        # Learn opponent's move
        c1.learn(move1, move2)
        c2.learn(move2, move1)

        # condition to determine Player1 victory scenario
        if beats(move1, move2):
            c1.win += 1
            print(f"Round Result\t: ** {c1.name} Wins **")
            self.winner = c1
            return self.winner
        # condition to determine game tie scenario
        elif move1 == move2:
            print("Round Result\t: ** Game Tie **")
            self.play_sub_round(c1, c2)
        # condition to determine Player2 victory scenario
        else:
            c2.win += 1
            print(f"Round Result\t: ** {c2.name} Wins **")
            self.winner = c2
            return self.winner
        # statement to display total score every round
        print(f"Score until now : {c1.name} "
              f"- {c1.win}, {c2.name} - {c2.win}")


    # Game method to play a match of several rounds
    def play_game(self):
        print("Game start!")
        # Case: player does not want to quit / play game again
        while self.game != "quit" and self.game != "no":
            self.round += 1
            print(f"\n[Round {self.round}]")
            self.play_round()
            self.game = input("\nPlay again? Type 'quit' to Quit > ").lower()
            # Condition to handle unrecognized input on 'self.game'
            while (self.game != "play again" and self.game != "yes") and \
                  (self.game != "quit" and self.game != "no"):
                self.game = input("Play again? Type 'quit' to Quit > ").lower()
        # function method to announce winner
        self.announce_winner()
        print("Game over!")

    # Game method to play a single round
    def play_game_once(self):
        print("Game Start!")
        self.play_round()
        print("Game over!")


# Case: If only Game executed directly
# if __name__ == '__main__':
    # Case1: For Game between 'Computer - (random move)' and User -
    # uncomment below line and comment out 'line 164' 'line 167' and 'line 170'
    # game = Game(Player(), HumanPlayer())
    # Case2: For Game between 'Computer - (Reflect User Moves)' and 'User' -
    # uncomment below line and comment out 'line 161' 'line 167' and 'line 170'
    # game = Game(ReflectPlayer(), HumanPlayer())
    # Case3: For Game between 'Computer - (Cycle Moves)' and 'User' -
    # uncomment below line and comment out 'line 161' 'line 164' and 'line 170'
    # game = Game(CyclePlayer(), HumanPlayer())
    # Case4: For Game between 'Contant move - (rock)' and 'User' -
    # uncomment below line and comment out 'line 161' 'line 164' and 'line 167'
    # game = Game(ConstantPlayer(), HumanPlayer())

    # Game method to play a match of several rounds -
    # uncomment below line and comment out 'line 177'
    # game.play_game()
    # Game method to play a single round -
    # uncomment below line and comment out 'line 174'
    # game.play_game_once()

if __name__ == '__main__':
    game = Game(HumanPlayer(), Player(), ReflectPlayer(), CyclePlayer())
    game.play_game()
