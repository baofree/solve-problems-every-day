def solution(n, stages):
    result = []
    stages.sort(reverse=True)
    for stage_num in range(n, 0, -1):
        total_player = 0
        clear_player = 0
        for index in range(len(stages)):
            if stage_num < stages[index]:
                total_player += 1
                clear_player += 1
            elif stage_num == stages[index]:
                total_player += 1
            else:
                break
        result.insert(0, {
            'state_id': stage_num,
            'error_rate': (total_player - clear_player) / total_player
        })
    result.sort(key=lambda ret: ret['error_rate'], reverse=True)
    return [x['state_id'] for x in result]


if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
    print(solution(4, [4, 4, 4, 4, 4]))  # [4,1,2,3]
