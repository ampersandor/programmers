def time_to_min(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(plans):
    finished = list()
    paused = list()
    plans.sort(key= lambda x: x[1])
    p = 0

    while p < len(plans):
        subject = plans[p][0]
        start = time_to_min(plans[p][1])
        duration = int(plans[p][2])
        nxt_start = time_to_min(plans[p+1][1]) if p < len(plans) - 1 else time_to_min("24:00")
        time_slot = nxt_start - start
        remaining_time = time_slot - duration
        if remaining_time >= 0:
            finished.append(subject)
        else:
            paused.append([subject, -remaining_time])
        while paused and remaining_time > 0:
            subject, duration = paused[-1]
            if duration <= remaining_time:
                finished.append(subject)
                remaining_time -= duration
                paused.pop()
            else:
                paused[-1][1] = duration - remaining_time
                break
        p += 1

    while paused:
        subject, duration = paused.pop()
        finished.append(subject)

    return finished
            
        
    


if __name__ == "__main__":
    # print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))

    print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))

    # solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]])