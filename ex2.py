from datetime import datetime

def solve(h1, m1, s1, h2, m2, s2):

    time1 = datetime.strptime(f"{h1}:{m1}:{s1}", "%H:%M:%S")
    time2 = datetime.strptime(f"{h2}:{m2}:{s2}", "%H:%M:%S")

    if time1 > time2:
        time_diff = time1 - time2
    else:
        time_diff = time2 - time1

    return time_diff.seconds