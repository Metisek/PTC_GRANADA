class ex2:
    def __init__(self, word, letter):
        if not isinstance(word, str):
            raise TypeError('String must be a string')
        if not isinstance(letter, str):
            raise TypeError('Letter must be a string')
        self.string = word
        self.letter = set(letter.lower())

    def solve_iteration(self):
        result = ''
        for char in self.string:
            temp_char = char
            if ord(temp_char) >= 65 and ord(temp_char) <= 90:
                temp_char = chr(ord(char) + 32)
            if temp_char not in self.letter:
                result += char
        return result

    def solve_method(self):
        return ''.join(filter(lambda char: char.lower() not in self.letter, self.string))


    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 2, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 2, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
