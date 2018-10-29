import re


def solution(dart_result):
    scores = re.findall(r"(\d+)(\w)(\*|#|)|", dart_result)
    answer = []
    for index in range(3):
        score = scores[index]
        point = int(score[0])
        bonus = score[1]
        option = score[2]
        if bonus == 'S':
            point = point ** 1
        elif bonus == 'D':
            point = point ** 2
        else:
            point = point ** 3
        answer.append(point)
        if option == '*':
            if index > 0:
                answer[index - 1] = answer[index - 1] * 2
            answer[index] = answer[index] * 2
        elif option == '#':
            answer[index] = answer[index] * -1
    return sum(answer)


if __name__ == '__main__':
    print(solution('1S2D*3T'))
    print(solution('1D2S#10S'))
    print(solution('1D2S0T'))
    print(solution('1S*2T*3S'))
    print(solution('1D#2S*3S'))
    print(solution('1T2D3D#'))
    print(solution('1D2S3T*'))
