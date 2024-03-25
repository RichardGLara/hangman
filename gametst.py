import os
import time

os.system('cls' if os.name == 'nt' else 'clear')
player = input(f"\t\tEnter player name: \n\t").title()
secret_word = input(f"\n\tEnter a word to be guessed: \n\t").upper()
tip = input(f"\tEnter a tip: \n\t")

os.system('cls' if os.name == 'nt' else 'clear')
            #print(f"\n\t{player}\n\t{secret_word}\n\t{tip}")

def list_letters():
    listing = list(secret_word)
            #print(listing)
    return listing


def count_letters():
    counting = len(secret_word)
            #print(counting)
    return counting


def create_board():
    board = ["_" for _ in range(count_letters())]
            #print(board)
    return board


def display_board():

    for ind in list_letters():
        print(f"{('|'.join)}")


display_board()
#print(create_board())
#list_letters()
#count_letters()