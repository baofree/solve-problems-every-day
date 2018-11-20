def solution(costs):
    current = 0
    case1 = 0
    case2 = 0

    for index in range(len(costs) - 1, -1, -1):
        current = costs[index] + min(case1, case2)
        case2 = case1
        case1 = current
    return min(case1, case2)
    pass


if __name__ == '__main__':
    print(solution([10, 15, 20]))
    print(solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
