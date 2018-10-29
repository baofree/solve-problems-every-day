import re


def get_str_list(str):
    result = []
    for index in range(len(str) - 1):
        val = str[index] + str[index + 1]
        if re.search(r'[a-z]{2}', val):
            result.append(val)
    return result


def get_intersection(list1, list2):
    result = []
    list1 = list1.copy()
    list2 = list2.copy()
    for x in list1:
        if x in list2:
            list2.remove(x)
            result.append(x)
    return result


def get_union(list1, list2):
    result = []
    list1 = list1.copy()
    list2 = list2.copy()

    for x in list1:
        if x in list2:
            list2.remove(x)
        result.append(x)

    for x in list2:
        result.append(x)
    return result


def solution(str1, str2):
    similarity = 1
    str1_list = get_str_list(str1.lower())
    str2_list = get_str_list(str2.lower())
    intersection = get_intersection(str1_list, str2_list)
    union = get_union(str1_list, str2_list)
    if len(intersection) > 0:
        similarity = len(intersection) / len(union)
    return int(similarity * 65536)


if __name__ == '__main__':
    print(solution('FRANCE', 'french'))
    print(solution('handshake', 'shake hands'))
    print(solution('aa1+aa2', 'AAAA12'))
    print(solution('E=M*C^2', 'e=m*c^2'))
