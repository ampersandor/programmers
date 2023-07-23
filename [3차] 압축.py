# https://school.programmers.co.kr/learn/courses/30/lessons/17684

from unittest import TestCase, main


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(solution("KAKAO"), [11, 1, 27, 15])
        self.assertEqual(solution("TOBEORNOTTOBEORTOBEORNOT"), [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])


def solution(msg):
    dictionary = {chr(i+64): i for i in range(1, 27)}
    if len(msg) == 1:
        return [dictionary[msg[0]]]
    answer = []
    num = 27
    i = 0
    while i < len(msg) - 1:
        start = i
        while msg[start:i+1] in dictionary and i < len(msg) - 1:
            i += 1
        word = msg[start:i+1]
        if word in dictionary:
            answer.append(dictionary[word])
            word = ""
        else:
            dictionary[word] = num
            num += 1
            answer.append(dictionary[word[:-1]])
    if word:
        answer.append(dictionary[msg[i]])
    return answer
    


if __name__ == "__main__":
    main()