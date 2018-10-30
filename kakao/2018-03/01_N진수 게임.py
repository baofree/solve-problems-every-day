def conversion(n, num):
    result = []
    if num == 0:
        return '0'
    while num != 0:
        a = num % n
        if a >= 10:
            a = chr(a + 55)
        else:
            a = str(a)
        result.append(a)
        num = int(num / n)
    result.reverse()
    return ''.join(result)


def solution(n, t, m, p):
    loop_count = t * m
    index = 0
    total_loop = 0
    result = []
    while index < loop_count or total_loop < loop_count:
        num = conversion(n, index)
        num_length = len(num)
        for k in range(num_length):
            if index >= loop_count or total_loop >= loop_count:
                break
            if (total_loop % m) + 1 == p:
                result.append(num[k])
            total_loop += 1
        index += 1
    return ''.join(result)


if __name__ == '__main__':
    print(solution(2, 4, 2, 1))  # “0111”
    print(solution(16, 16, 2, 1))  # “02468ACE11111111”
    print(solution(16, 16, 2, 2))  # “13579BDF01234567”
