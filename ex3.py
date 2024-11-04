from exercise_class_init import Exercise
import re

class ex3(Exercise):
    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError('Text argument must be a string')
        self.text = text
        super().__init__()

    def solve(self):
        words = re.findall(r'\b\w+\b', self.text.lower())
        frequency = {}

        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

        most_frequent = sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:3]
        return [word for word, count in most_frequent]

