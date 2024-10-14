class ex5:
    def __init__(self, word):
        if not isinstance(word, str):
            raise TypeError('String must be a string')
        self.string = word
        self.vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def solve_iteration(self):
        result = 0
        for char in self.string:
            for vovel in self.vovels:
                if char == vovel:
                    result += 1
                    break
        return result

    def solve_method(self):
        return sum(1 for char in self.string if char in self.vovels)

    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 5, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 5, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
