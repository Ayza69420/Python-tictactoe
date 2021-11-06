from os import system
from random import choice
from colorama import Fore as FORE

class tictactoe:
    def __init__(self):
        self.board = ['-' for _ in range(10)]
        self.turn = 'X'
        self.playing = True

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def win_check(self):
        possible_winning_methods = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        for i in possible_winning_methods:
            if self.board[i[0]] == self.turn and self.board[i[1]] == self.turn and self.board[i[2]] == self.turn:
                return True
        return False
    
    def display_board(self):
        print(
f'''  
{'='*(len(self.board)-1)}
{self.board[0]} | {self.board[1]} | {self.board[2]}
{self.board[3]} | {self.board[4]} | {self.board[5]}
{self.board[6]} | {self.board[7]} | {self.board[8]}
{'='*(len(self.board)-1)}
'''
)

    def check_for_availbility(self,index):
        try:
            if self.board[index-1] == '-': 
                return True
            return False
        except IndexError:
            return 'Input a valid index.'

    def change_index(self,index):
        try:
            self.board[index-1] = self.turn
        except IndexError:
            print('Input a valid index.')

    def player_input(self):
        colors = [FORE.BLUE,FORE.CYAN,FORE.GREEN,FORE.LIGHTRED_EX,FORE.LIGHTMAGENTA_EX]

        return input(f'{choice(colors)}[{self.turn}]{FORE.RESET} Pick an index to play in\n')

    def main_game(self):
        while self.playing:
            system('cls')

            self.display_board()

            place = self.player_input()

            try:
                available = self.check_for_availbility(int(place))
                if available:
                    self.change_index(int(place))
                elif not available:
                    print('That place is already taken.')
                else:
                    print(available)

                if self.win_check():
                    print(f'{self.turn} has won the game!')
                    self.playing = False
                    
                self.change_turn()
                continue

            except ValueError:
                print('Input an integer')
                continue

game = tictactoe()

game.main_game()
