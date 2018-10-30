import re


def solution(words):
    learning_word = '-'.join(words)
    result = 0
    for word in words:
        for index in range(len(word)):
            result += 1
            if len(re.findall(word[:index + 1], learning_word)) == 1:
                break
    return result


if __name__ == '__main__':
    print(solution(["go", "gone", "guild"]))  # 7
    print(solution(["abc", "def", "ghi", "jklm"]))  # 4
    print(solution(["word", "war", "warrior", "world"]))  # 15
