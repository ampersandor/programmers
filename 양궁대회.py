def backtracking(cur, n, apache_board, lion_board, apache, lion, answer):
    diff = lion - apache
    if n == 0 and diff > 0 and (diff > answer[0] or (diff == answer[0] and lion_board[::-1] > answer[1][::-1])):
        answer[0] = diff
        answer[1] = lion_board[:]
        return
    for i in range(cur, len(apache_board)):
        if n > apache_board[i]:
            if apache_board[i] != 0:
                apache -= (10 - i)
            lion += (10 - i)
            lion_board[i] = (apache_board[i] + 1)
            backtracking(i + 1, n - (apache_board[i] + 1), apache_board, lion_board, apache, lion, answer)
            lion_board[i] = 0
            if apache_board[i] != 0:
                apache += (10 - i)
            lion -= (10 - i)
        elif i == len(apache_board) - 1:
            lion_board[i] = n
            backtracking(i + 1, 0, apache_board, lion_board, apache, lion, answer)
            lion_board[i] = 0

def solution(n, info):
    answer = [-1, [-1]]
    lion_board = [0] * len(info)
    apache = sum(map(lambda i: (10 - i) if info[i] > 0 else 0, range(11)))
    backtracking(0, n, info, lion_board, apache, 0, answer)

    return answer[1]


if __name__ == "__main__":
    n = 5
    info = [2,1,1,1,0,0,0,0,0,0,0]
    print(solution(n, info))

    n = 1
    info = [1,0,0,0,0,0,0,0,0,0,0]
    print(solution(n, info))

    n = 9
    info = [0,0,1,2,0,1,1,1,1,1,1]
    print(solution(n, info))

    n = 10
    info = [0,0,0,0,0,0,0,0,3,4,3]
    print(solution(n, info))