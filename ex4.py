class ex4:
    def __init__(self, word, subword):
        if not isinstance(word, str):
            raise TypeError('String must be a string')
        if not isinstance(subword, str):
            raise TypeError('Subword must be a string')
        self.string = word
        self.substring = subword

    def solve_iteration(self):
        result = -1
        for i in range(len(self.string) - len(self.substring) + 1):
            if self.string[i:i + len(self.substring)] == self.substring:
                result = i
                break
        return result

    def solve_method(self):
        return self.string.find(self.substring)

    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 4, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 4, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
