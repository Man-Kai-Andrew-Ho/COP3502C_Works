def initialize_board(num_rows, num_cols):
    board = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append("-")
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for item in row:
            if item == len(row) - 1:
                print(item, end="")
            else:
                print(item, end=" ")
        print()

def insert_chip(board, col, chip_type):
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == "-":
            board[row][col] = chip_type
            return row
    return -1

def check_if_winner(board, col, row, chip_type):
    num_rows = len(board)
    num_cols = len(board[0])
    win = 4

    count = 0
    for c in range(num_cols):
        if board[row][c] == chip_type:
            count += 1
            if count == win:
                return True
        else:
            count = 0

    count = 0
    for r in range(num_rows):
        if board[r][col] == chip_type:
            count += 1
            if count == win:
                return True
        else:
            count = 0

    count = 0
    start_row, start_col = row, col
    while start_row > 0 and start_col > 0:
        start_row -= 1
        start_col -= 1
    while start_row < num_rows and start_col < num_cols:
        if board[start_row][start_col] == chip_type:
            count += 1
            if count == win:
                return True
        else:
            count = 0
        start_row += 1
        start_col += 1

    count = 0
    start_row, start_col = row, col
    while start_row < num_rows - 1 and start_col > 0:
        start_row += 1
        start_col -= 1
    while start_row >= 0 and start_col < num_cols:
        if board[start_row][start_col] == chip_type:
            count += 1
            if count == win:
                return True
        else:
            count = 0
        start_row -= 1
        start_col += 1

    return False

def is_draw(board):
    return all(board[0][col] != "-" for col in range(len(board[0])))

if __name__ == "__main__":
    rows = int(input("What would you like the height of the board to be? "))
    cols = int(input("What would you like the length of the board to be? "))
    p1, p2 = "x", "o"

    board_set = initialize_board(rows, cols)
    print_board(board_set)
    print()
    print(f"Player 1: {p1}")
    print(f"Player 2: {p2}")
    print()
    count = 1


    while True:
        if count % 2 != 0:
            p1_col = int(input("Player 1: Which column would you like to choose? "))
            row = insert_chip(board_set, p1_col, p1)
            if row == -1:
                print("Column full! Choose another column.")
                continue
            print_board(board_set)
            print()
            if check_if_winner(board_set, p1_col, row, p1):
                print("Player 1 won the game!")
                break
        else:
            p2_col = int(input("Player 2: Which column would you like to choose? "))
            row = insert_chip(board_set, p2_col, p2)
            if row == -1:
                print("Column full! Choose another column.")
                continue
            print_board(board_set)
            print()
            if check_if_winner(board_set, p2_col, row, p2):
                print("Player 2 won the game!")
                break

        if is_draw(board_set):
            print("Draw. Nobody wins.")
            break

        count += 1
