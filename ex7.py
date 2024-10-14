class ex7:
    def __init__(self, word):
        if not isinstance(word, str):
            raise TypeError('String must be a string')
        self.string = word

    def solve_iteration(self):
        for i in range(0, len(self.string)):
            if ord(self.string[i]) >= ord('a') and ord(self.string[i]) <= ord('z'):
                self.string = self.string[:i] + chr(ord(self.string[i]) - 32) + self.string[i + 1:]
        return self.string

    def solve_method(self):
        return self.string.upper()

    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 7, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 7, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
