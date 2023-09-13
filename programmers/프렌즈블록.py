from collections import defaultdict


def solution(m, n, board):
    answer = 0
    board = list(map(list, board)) # convert string to list in board item
    
    while True:
        tbr = defaultdict(set)
        removed = 0
        for i in range(m-1): # find and update all the indices to be removed.
            for j in range(n-1):
                if board[i][j] != "" and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    tbr[j].update({i, i+1})
                    tbr[j+1].update({i, i+1})

        for col, rows in tbr.items():
            cur = m-1
            row = m-1
            removed += len(rows)
            while row > -1: # rewrite from the bottom
                if row not in rows:
                    board[cur][col] = board[row][col]
                    cur -= 1
                row -= 1
            while cur > -1: # wipe out the above
                board[cur][col] = ""
                cur -= 1
        if removed == 0:
            break
            
        answer += removed
        
    
    return answer

# "CCBDE 
# "AAADE
# "AAABF 
# "CCBBF