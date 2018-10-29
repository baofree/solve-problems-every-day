def solution(n, map1, map2):
    result = []
    for a, b in zip(map1, map2):
        result.append(str(bin(a | b)[2:].zfill(n)).replace('1', '#').replace('0', ' '))
    return result


if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
