from datetime import timedelta

def solve(time1: str, time2: str) -> str:
    try:
        if len(time1.split(':')) == 2:
            time1 += ':00'
        if len(time2.split(':')) == 2:
            time2 += ':00'
    except Exception as e:
        return f"Error: {e}"

    h1, m1, s1 = map(int, time1.split(':'))
    h2, m2, s2 = map(int, time2.split(':'))

    t1 = timedelta(hours=h1, minutes=m1, seconds=s1)
    t2 = timedelta(hours=h2, minutes=m2, seconds=s2)

    diff = abs(t2 - t1)

    return str(diff)