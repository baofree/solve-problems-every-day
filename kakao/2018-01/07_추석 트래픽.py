import datetime


def solution(logs):
    log_data = []
    max_count = 0
    for log in logs:
        date, time, t = log.split(' ')
        t = float(t.replace('s', '')) * 1000
        end_log = datetime.datetime.strptime("%s %s" % (date, time), "%Y-%m-%d %H:%M:%S.%f")
        start_log = end_log - datetime.timedelta(milliseconds=t - 1)
        log_data.append({
            'start': start_log,
            'end': end_log,
        })
    for line in log_data:
        start = line['end']
        end = line['end'] + datetime.timedelta(milliseconds=999)
        count = 0
        for a in log_data:
            if a['start'] <= start <= a['end'] or a['start'] <= end <= a['end']:
                count += 1
        max_count = max(count, max_count)
    return max_count


if __name__ == '__main__':
    print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
    print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
    print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
                    "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
                    "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s",
                    "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
