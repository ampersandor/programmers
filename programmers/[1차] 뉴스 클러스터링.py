from collections import defaultdict


def solution(str1, str2):
    answer = 0
    my_dict = defaultdict(int)
    total = 0
    for i in range(len(str1) - 1):
        word = str1[i:i+2].lower()
        if word.isalpha():
            my_dict[word] += 1
            total += 1
    for i in range(len(str2) - 1):
        word = str2[i:i+2].lower()
        if word.isalpha():
            if my_dict[word] > 0:
                answer += 1
                my_dict[word] -= 1
            else:
                total += 1
        
    return 65536 if total == 0 else int(answer / total * 65536)
