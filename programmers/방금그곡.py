def to_min(clock):
    hour, minute = map(int, clock.split(":"))
    
    return hour * 60 + minute


def parse(notes):
    res = []
    for note in notes:
        if note.isalpha():
            res.append(note)
        else:
            res[-1] = res[-1].lower()
            
    return "".join(res)


def solution(m, musicinfos):
    answer = None
    m = parse(m)
    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(",")
        duration = to_min(end) - to_min(start)
        code = parse(code)
        code = (code * ((duration + len(code) - 1) // len(code)))[:duration]
        if m in code and (not answer or duration > answer[0]):
            answer = (duration, title)
    
    return answer[-1] if answer else "(None)"