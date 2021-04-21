board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

boardkeys = []

for key in board :
    boardkeys.append(key)


def printboard(board) :

    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print("--+---+--")

    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print("--+---+--")

    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])


def game():
    turn = 'X'
    count = 0

    for i in range(1,10):
        printboard(board)

        print("IT IS TURN OF " + turn + " SPECIFY THE CELL YOU WANT TO PLAY : ")

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else :
            print("SORRY THIS CELL LOCATION IS FILLED. PLEASE CHOOSE ANOTHER CELL ")
            continue

        if count >= 5 :
            if board['1'] == board['2'] == board['3'] != ' ' :
                printboard(board)
                print("\n GAME OVER \n ")
                print("Player " + turn + " WON the game")

                break

            if board['4'] == board['5'] == board['6'] != ' ' :
                printboard(board)
                print("\n GAME OVER \n ")
                print("Player " + turn + " WON the game")

                break

            if board['7'] == board['8'] == board['9'] != ' ' :
                printboard(board)
                print("\n GAME OVER \n ")
                print("Player " + turn + " WON the game")

                break

            if board['1'] == board['4'] == board['7'] != ' ' :
                printboard(board)
                print("\n GAME OVER \n ")
                print("Player " + turn + " WON the game")

                break

            if board['2'] == board['5'] == board['8'] != ' ' :
                printboard(board)
                print("\n GAME OVER \n ")
                print("Player " + turn + " WON the game")

                break

            if board['3'] == board['6'] == board['9'] != ' ' :
                printboard(board)
                print("\n GAME OVER \n ")
                print("Player " + turn + " WON the game")

                break

            if board['1'] == board['5'] == board['9'] != ' ' :
                printboard(board)
                print("\n GAME OVER \n ")
                print("Player " + turn + " WON the game")

                break

            if board['3'] == board['5'] == board['7'] != ' ' :
                printboard(board)
                print("\n GAME OVER \n ")
                print("Player " + turn + " WON the game")

                break

        if count == 9 :
            print("\n GAME OVER !!! \n")
            print("GAME WAS A TIE!!! ")

        if turn == "X" :
            turn = "0"
        else :
            turn = "X"

    restart = input("DO YOU WANT TO PLAY AGAIN ? (Y/N) ")

    if restart == "y" or restart == "Y" :
        for key in boardkeys :
            board[key] = ' '

        game()

if __name__ == "__main__" :
    game()
