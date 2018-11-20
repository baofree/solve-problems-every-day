def merge(a, b):
    temp = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            temp.append(a.pop(0))
        else:
            temp.append(b.pop(0))

    if len(a) == 0:
        temp += b
    else:
        temp += a
    return temp


def sort(data):
    if len(data) == 0 or len(data) == 1:
        return data
    mid = len(data) // 2
    a = sort(data[:mid])
    b = sort(data[mid:])
    return merge(a, b)


if __name__ == '__main__':
    data = [x for x in range(10, 0, -1)]
    print(sort(data))
