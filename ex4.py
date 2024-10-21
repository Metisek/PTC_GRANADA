from exercise_class_init import Exercise

class ex4(Exercise):
    def __init__(self, dictionary):
        if not isinstance(dictionary, dict):
            raise TypeError('Argument must be a dictionary')
        self.dictionary = dictionary
        super().__init__()

    def solve(self):
        reversed_dict = {}
        for key, value in self.dictionary.items():
            if value in reversed_dict:
                raise ValueError('Duplicate values found in the dictionary')
            reversed_dict[value] = key
        return reversed_dict