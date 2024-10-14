class ex6:
    def __init__(self, word):
        if not isinstance(word, str):
            raise TypeError('String must be a string')
        self.string = word
        self.vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def solve_iteration(self):
        result = []
        for char in self.string:
            for vovel in self.vovels:
                if char == vovel:
                    if ord(char) >= 65 and ord(char) <= 90:
                        char = chr(ord(char) + 32)
                    result.append(char)
        return set(result)

    def solve_method(self):
        return set(filter(lambda char: char.lower() in self.vovels, self.string))

    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 6, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 6, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
