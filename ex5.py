from exercise_class_init import Exercise
from collections import defaultdict

class ex5(Exercise):
    def __init__(self, log):
        if not isinstance(log, str):
            raise TypeError('Text argument must be a string')
        self.text = log
        super().__init__()

    def solve(self):
        summary = defaultdict(lambda: defaultdict(int))
        logs = self.text.split('\n')

        for log in logs:
            user, action = log.split(':')
            summary[user][action] += 1

        return {user: dict(actions) for user, actions in summary.items()}