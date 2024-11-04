from exercise_class_init import Exercise

class ex8(Exercise):
    def __init__(self, temperature_dict):
        if not isinstance(temperature_dict, dict):
            raise TypeError('Temperature argument must be a dictionary')
        for key, value in temperature_dict.items():
            if not isinstance(key, str) or not isinstance(value, int):
                raise TypeError('Dictionary keys must be strings and values must be integers')
        self.temperature_dict = temperature_dict
        super().__init__()

    def solve(self):
        result = {}
        for city, temp in self.temperature_dict.items():
            if temp not in result:
                result[temp] = []
            result[temp].append(city)
        result = {temperature : sorted(cities) for temperature, cities in result.items()}
        result = dict(sorted(result.items()))
        return result