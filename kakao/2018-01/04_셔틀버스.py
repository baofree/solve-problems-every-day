import datetime


def str_to_time(str):
    return datetime.datetime.strptime(str, "%H:%M")


def get_info(time_table, bus_time, m):
    take_count = 0
    take_time = []
    pass
    for time in time_table:
        if take_count == m or str_to_time(time) > bus_time:
            break
        take_time.append(time)
    for time in take_time:
        time_table.remove(time)
    return {
        'time': bus_time,
        'takes': take_time
    }


def solution(n, t, m, time_table):
    time_table.sort()
    bus_time = str_to_time('09:00')
    bus_info = []
    for num in range(n):
        bus_info.append(get_info(time_table, bus_time, m))
        bus_time += datetime.timedelta(minutes=t)
    last_bus = bus_info[-1]
    if len(last_bus['takes']) < m:
        return last_bus['time'].strftime("%H:%M")
    return (str_to_time(last_bus['takes'][-1]) + datetime.timedelta(minutes=-1)).strftime("%H:%M")


if __name__ == '__main__':
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(solution(1, 1, 1, ["23:59"]))
    print(solution(10, 60, 45,
                   ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                    "23:59", "23:59", "23:59", "23:59", "23:59"]))
