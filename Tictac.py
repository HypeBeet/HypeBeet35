#Tic Tac Toe

import random
new = ['','','','','','','','','']
man = ''
machine = ''
null = ''


def sign(man, machine):
    man = raw_input("Ps or Qs, mind your Ps and Qs? Q or P ")
    while man not in ('Q','q','p','P'):
        print ("Do not do that Mr. Roaden")
        man = raw_input("Ps or Qs, mind your Ps and Qs? Q or P ")
    if man == 'q' or man == 'Q':
        print ("You are the Q team, mind your Qs and Ps.")
        machine = 'P'
    else:
        print ("you are the P team.")
        machine = 'Q'
    return man.upper(), machine.upper()


def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_combinations = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (3, 6, 9), (1, 4, 7), (2, 5, 8), (1, 5, 9), (3, 5, 7 ))

    def draw():
        print(board[1], board[2], board[3])
        print(board[4], board[5], board[6])
        print(board[7], board[8], board[9])
        print()

def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(1, 9):
                        return a
                        continue

def check_board():
        	count = 0
       	 for a in win_combinations:
            if board[a[1]] == board[a[2]] == board[a[3]] == "P":
                print("Big Dub to P\n")
                print("You watched your Ps and Qs, Roadmeister\n")
                return True

            if board[a[1]] == board[a[2]] == board[a[3]] == "Q":
                print("Big Dub to Q\n")
                print("You watched your Ps and Qs, Roadmeister\n")
                return True
        for a in range(9):
            if board[a] == "P" or board[a] == "Q":
                count += 1
            if count == 9:
                print("CAT, Neither watched their Ps or Qs\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Playa 1, Place a P")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Playa 2, place a Q")
        p2()
        print()


tic_tac_toe()



