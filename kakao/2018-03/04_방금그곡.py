import re


def conversion(melody):
    return re.sub(r'([A-Z])\#', lambda match: match.group(1).lower(), melody)


def get_time(time):
    min, sec = time.split(':')
    return int(min) * 60 + int(sec)


def get_play_time(start, end):
    start_time = get_time(start)
    end_time = get_time(end)
    return end_time - start_time


def solution(melody, music_infos):
    melody = conversion(melody)
    result = None
    result_play_time = 0
    for music_info in music_infos:
        start, end, name, code = music_info.split(',')
        code = conversion(code)
        play_time = get_play_time(start, end)
        play_melody = ''
        for i in range(play_time):
            index = i % len(code)
            play_melody += code[index]
        if re.findall(melody, play_melody):
            if play_time > result_play_time:
                result = name
    return result


if __name__ == '__main__':
    print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))  # “HELLO”
    print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))  # “FOO”
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))  # “WORLD”
