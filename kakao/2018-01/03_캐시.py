import time


def solution(cache_size, cities):
    cache = {}

    def get(city):
        city = city.lower()
        if city in cache:
            cache[city] = time.time()
            return 1
        if len(cache) == cache_size:
            base = time.time()
            delete_key = None
            for key in cache:
                if cache[key] < base:
                    base = cache[key]
                    delete_key = key
            cache.pop(delete_key, None)
        if cache_size > 0:
            cache[city] = time.time()
        return 5

    total_time = 0
    for city in cities:
        total_time += get(city)
    return total_time


if __name__ == '__main__':
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                       "NewYork", "Rome"]))
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                       "NewYork", "Rome"]))
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
