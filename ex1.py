class ex1:
    def __init__(self, string):
        if not isinstance(string, str):
            raise TypeError('String must be a string')
        self.string = string

    def solve_iteration(self):
        count = 0
        for _ in self.string:
            count += 1
        return count

    def solve_method(self):
        return len(self.string)

    def compare(self):
        return self.solve_iteration() == self.solve_method()

    def run(self):
        print("Exercise 1, Method 1: Iteration", end=' ')
        print(self.solve_iteration())
        print("Exercise 1, Method 2: String method", end=' ')
        print(self.solve_method())
        if self.compare():
            print('Both methods are equal')
        else:
            print('Methods are not equal')
