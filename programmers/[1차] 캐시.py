# https://school.programmers.co.kr/learn/courses/30/lessons/17680

from unittest import TestCase, main


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]), 50)
        self.assertEqual(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]), 21)
        self.assertEqual(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]), 60)
        self.assertEqual(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]), 52)
        self.assertEqual(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]), 16)
        self.assertEqual(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]), 25)    


def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        try:
            idx = cache.index(city)
            answer += 1
            cache.pop(idx)
        except:
            answer += 5
        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)

    return answer


if __name__ == "__main__":
    main()