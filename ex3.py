class ex3:
    def __init__(self, word):
        if not isinstance(word, str):
            raise TypeError('String must be a string')
        self.string = word

    def solve_iteration(self):
        result = ''
        for char in self.string:
            chat_idx = ord(char)
            if 65 <= chat_idx <= 90:
                chat_idx += 32
            elif 97 <= chat_idx <= 122:
                chat_idx -= 32
            result += chr(chat_idx)
        return result

    def solve_method(self):
        return self.string.swapcase()

    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 3, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 3, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
