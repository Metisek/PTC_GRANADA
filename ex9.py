class ex9:
    def __init__(self, word):
        if not isinstance(word, str):
            raise TypeError('String must be a string')
        self.string = word
        self.vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def solve_iteration(self):
        result = ''
        for char in self.string:
            if char not in self.vovels:
                result += char
        return result

    def solve_method(self):
        return ''.join(filter(lambda char: char.lower() not in self.vovels, self.string))

    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 9, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 9, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
