class Exercise:
    def __init__(self, *args):

        self.exercise_name = self.__class__.__name__

    def solve(self):
        pass

    def print_result(self):
        print("Window renderend properly (function completed with exit code 0)")

    def run(self):
        print("Exercise {} result:".format(self.exercise_name))
        self.solve()
        self.print_result()
