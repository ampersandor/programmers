def solution(n):
    answer = [[0] * x for x in range(1, n + 1)]
    tot = sum(range(1, n + 1))
    i, j = 0, 0
    d = 0
    for n in range(1, tot + 1):
        answer[i][j] = n
        # print(answer)
        if d == 0 and ((i + 1) == len(answer) or answer[i+1][j] != 0):
            d = 1
        elif d == 1 and ((j + 1) == len(answer[i]) or answer[i][j+1] != 0):
            d = 2
        elif d == 2 and answer[i-1][j-1] != 0:
            d = 0
            
        if d == 0:
            i += 1
        elif d == 1:
            j += 1
        elif d == 2:
            i -= 1
            j -= 1
        
    return [x for y in answer for x in y]

if __name__ == "__main__":
    n = 4
    print(solution(n))
    # n = 5
    # print(solution(n))
    # n = 6
    # print(solution(n))