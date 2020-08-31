# write your code here
# input_list = input("Enter cells: ")  # take input
input_list = '_________'
matrix = [list(input_list[:3]), list(input_list[3:6]), list(input_list[6:])]  # convert input into matrix
turn = ['X', 'O']
x_count = 0

# print matrix
print("---------")
for i in matrix:
    print("| ", end="")
    for val in i:
        print(val + " ", end="")
    print("|")
print("---------")

valid_move = False
while (not valid_move):
    for row in matrix:  # check if 3-in-a-row
        if row == ['X', 'X', 'X']:
            print("X wins")
            valid_move = True
        elif row == ['O', 'O', 'O']:
            print("O wins")
            valid_move = True
    if matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X':  # check if 3-in-a-diagonal
        print("X wins")  # 3 X's in left diagonal
        valid_move = True
    elif matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix [2][0] == 'X':
        print("X wins")  # 3 X's in right diagonal
        valid_move = True
    elif matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O':
        print("O wins")  # 3 O's in left diagonal
        valid_move = True
    elif matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix [2][0] == 'O':
        print("O wins")  # 3 O's in right diagonal
        valid_move = True
    elif matrix[0][0] == 'X' and matrix[1][0] == 'X' and matrix[2][0] == 'X':  # check if 3-in-a-column
        print("X wins")  # 3 X's in first column
        valid_move = True
    elif matrix[0][1] == 'X' and matrix[1][1] == 'X' and matrix[2][1] == 'X':
        print("X wins")  # 3 X's in second column
        valid_move = True
    elif matrix[0][2] == 'X' and matrix[1][2] == 'X' and matrix[2][2] == 'X':
        print("X wins")  # 3 X's in third column
        valid_move = True
    elif matrix[0][0] == 'O' and matrix[1][0] == 'O' and matrix[2][0] == 'O':
        print("O wins")  # 3 O's in first column
        valid_move = True
    elif matrix[0][1] == 'O' and matrix[1][1] == 'O' and matrix[2][1] == 'O':
        print("O wins")  # 3 O's in second column
        valid_move = True
    elif matrix[0][2] == 'O' and matrix[1][2] == 'O' and matrix[2][2] == 'O':
        print("O wins")  # 3 O's in third column
        valid_move = True
    else:
        # check if moves left
        x_count = 0
        for row in matrix:
            for column in row:
                if column == 'X':
                    x_count += 1
        if x_count == 5:
            print("Draw")
            valid_move = True
        else:    
            next_move = input("Enter the coordinates: ")  # get next move
            next_move = next_move.split()
            real_move = ["", ""]
            if next_move[0] in "0123456789" and next_move[1] in "0123456789":  # check if numerical input
                if next_move[0] in "123" and next_move[1] in "123":  # check if input within range
                    real_move[1] = int(next_move[0]) - 1
                    if next_move[1] == "3":
                        real_move[0] = 0
                    elif next_move[1] == "2":
                        real_move[0] = 1
                    else:
                        real_move[0] = 2
                    if matrix[real_move[0]][real_move[1]] == '_':  # check if cell occupied
                        matrix[real_move[0]][real_move[1]] = matrix[real_move[0]][real_move[1]].replace('_', turn[0])  # modify matrix
                        if turn[0] == 'X':
                            turn[0] == 'O'
                        else:
                            turn[0] == 'X'
                        print("---------")
                        for i in matrix:
                            print("| ", end="")
                            for val in i:
                                print(val + " ", end="")
                            print("|")
                        print("---------")
                        # valid_move = True
                    else:
                        print("This cell is occupied! Choose another one!")
                else:  # input out of range
                    print("Coordinates should be from 1 to 3!")
            else:  # input is not numerical
                print("You should enter numbers!")
