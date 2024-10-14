class ex10:
    def __init__(self, word1, word2):
        if not isinstance(word1, str):
            raise TypeError('Word1 must be a string')
        if not isinstance(word2, str):
            raise TypeError('Word2 must be a string')
        self.string1 = word1
        self.string2 = word2

    def solve_iteration(self):
        return self.string1 == self.string2[::-1]

    def solve_method(self):
        return self.string1 == ''.join(reversed(self.string2))

    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 10, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 10, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
