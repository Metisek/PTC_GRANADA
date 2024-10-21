from exercise_class_init import Exercise

class ex1(Exercise):
    def __init__(self, list_vals, diviser):
        if not isinstance(list_vals, list) and not isinstance(list, tuple):
            raise TypeError('List argument must be a valid list or tuple')
        if not isinstance(diviser, int):
            raise TypeError('Diviser argument must be an integer')
        self.list_vals = list_vals
        self.diviser = diviser
        super().__init__()

    def solve(self):
        sublists = [self.list_vals[i:i + self.diviser] for i in range(0, len(self.list_vals), self.diviser)]
        return sublists

