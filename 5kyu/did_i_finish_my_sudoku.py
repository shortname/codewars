def done_or_not(board): #board[i][j]
    rows = all(len(set(r)) == len(r) for r in board)
    columns = all(len(set(r)) == len(r) for r in zip(*board))
    squared = [board[3*i][3*j:3*(j+1)] + board[3*i+1][3*j:3*(j+1)] + board[3*i+2][3*j:3*(j+1)] for j in range(3) for i in range(3)]
    squares = all(len(set(r)) == len(r) for r in squared)
    if rows and columns and squares:
        return 'Finished!'
    else:
        return 'Try again!'