"""
길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
단계 2로 돌아간다.
"""


def init_dic():
    dic = {}
    for i in range(26):
        dic[chr(i + 65)] = i + 1
    return dic


def find(ch, dic):
    return [x for x in dic.keys() if x.startswith(ch)]


def solution(msg):
    dic = init_dic()
    last_index = 27
    result = []
    index = 0
    while index < len(msg):
        large_match = 0
        match_ch = None
        for in_ch in find(msg[index], dic):
            if msg[index:].startswith(in_ch) and large_match < len(in_ch):
                large_match = len(in_ch)
                match_ch = in_ch
        result.append(dic[match_ch])
        dic[msg[index:large_match + index + 1]] = last_index
        last_index += 1
        index += large_match
    return result


if __name__ == '__main__':
    # print('AB'.startswith('ABC'))
    print(solution('KAKAO'))  # [11, 1, 27, 15]
    print(solution('TOBEORNOTTOBEORTOBEORNOT'))  # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    print(solution('ABABABABABABABAB'))  # [1, 2, 27, 29, 28, 31, 30]
