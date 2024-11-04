from exercise_class_init import Exercise

class ex2(Exercise):
    def __init__(self, list_vals, number):
        if not isinstance(list_vals, list) and not isinstance(list_vals, tuple):
            raise TypeError('List argument must be a valid list or tuple')
        for i in list_vals:
            if not isinstance(i, int):
                raise TypeError('List must contain only integers')
        if not isinstance(number, int):
            raise TypeError('Number must be an integer')
        self.list_vals = list_vals
        self.number = number
        super().__init__()

    def solve(self):
        result = []
        for start in range(len(self.list_vals)):
            current_sum = 0
            sublist = []
            for end in range(start, len(self.list_vals)):
                current_sum += self.list_vals[end]
                sublist.append(self.list_vals[end])
                if current_sum == self.number:
                    result.append(sublist[:])
                    break
                elif current_sum > self.number:
                    break
        return result