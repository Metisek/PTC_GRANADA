from exercise_class_init import Exercise
import csv

class ex9(Exercise):
    def __init__(self, filename):
        self.filename = filename
        super().__init__()

    def read_csv(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            try:
                next(reader)  # Skip header
            except StopIteration:
                return {} # Empty file
            dictionary1 = {rows[0]: rows[1] for rows in reader}
        return dictionary1

    def read_csv_dict(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            dictionary2 = {row['Country']: row['Capital'] for row in reader}
        return dictionary2

    def solve(self):
        result_1 = self.read_csv()
        result_2 = self.read_csv_dict()
        return result_1, result_2

    def print_result(self, result):
        print("First dictionary from csv:")
        print(result[0])
        print("Second dictionary using DictReader:")
        print(result[1])