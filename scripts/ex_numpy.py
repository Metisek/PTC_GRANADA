import csv
import numpy as np

out_file_path = "csv_out/numpy_defensa.csv"

def exec(gdp_file_path, countries_file_path):
    data = load_gdp_data(gdp_file_path)
    countries = load_countries_data(countries_file_path)
    average_gdp_data = calculate_average_gdp(data, countries)
    save_to_csv(average_gdp_data, out_file_path)

def load_gdp_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            country_code = row['CCA3']
            year = int(row['Año'])
            gdp = float(row['PIB ($)'])
            if year in range(2015, 2023):
                data.append([country_code, year, gdp])
        return np.array(data, dtype=object)

def load_countries_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        countries = {}
        for row in reader:
            key = row[0][:3]
            val = row[0][3:]
            countries[key] = val
    return countries

def calculate_average_gdp(data, countries):
    unique_countries = np.unique(data[:, 0])
    result = []
    for country in unique_countries:
        country_data = data[data[:, 0] == country]
        gdp_values = country_data[:, 2].astype(float)
        average_gdp = np.mean(gdp_values)
        country_name = countries.get(country, country)
        result.append([country_name, average_gdp])
    return result

def save_to_csv(data, file_path):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Country', 'Average GDP (2015-2022)'])
        writer.writerows(data)