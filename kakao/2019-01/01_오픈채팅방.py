from string import Template


def solution(record):
    user_map = {}
    result_str = ''
    for event in record:
        event_data = event.split(' ')
        action = event_data[0]
        uid = event_data[1]
        if action == 'Enter':
            user_map[uid] = event_data[2]
            result_str += '$%s님이 들어왔습니다.|' % uid
        elif action == 'Change':
            user_map[uid] = event_data[2]
        else:
            result_str += '$%s님이 나갔습니다.|' % uid
    return Template(result_str).substitute(user_map).split('|')[:-1]


if __name__ == '__main__':
    print(solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
    # [“Prodo님이들어왔습니다.”, “Ryan님이 들어왔습니다.”, “Prodo님이 나갔습니다.”, “Prodo님이 들어왔습니다.”]
