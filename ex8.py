class ex8:
    def __init__(self, word):
        if not isinstance(word, str):
            raise TypeError('String must be a string') # I just realised it's nonsense, but it's staing because it's funny
        # THE FLOOR IS MADE OUT OF FLOOR
        self.string = word
        self.vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def solve_iteration(self):
        return self.string[0] in self.vovels and self.string[-1] in self.vovels

    def solve_method(self):
        # Well, it's gonna be identical to the iteration method
        # I don't think there is a method for that exercise
        return self.string[0] in self.vovels and self.string[-1] in self.vovels

    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 8, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 8, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
