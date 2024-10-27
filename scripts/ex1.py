import csv

# Load data from files
gdp_data = {}
population_data = {}

out_file_path = 'csv_out/gdp_per_capita.csv'


def exec(gdp, population, countries):
    with open(gdp, 'r', encoding='utf-8') as gdp_file:
        reader = csv.DictReader(gdp_file)
        for row in reader:
            if row['Año'] == '2022':
                gdp_data[row['CCA3']] = float(row['PIB ($)'])

    with open(population, 'r', encoding='utf-8') as pop_file:
        reader = csv.DictReader(pop_file)
        for row in reader:
            if '2022 Population' in row:
                population_data[row['CCA3']] = int(row['2022 Population'])

    # Calculate GDP per capita
    gdp_per_capita = []
    with open(countries, 'r', encoding='utf-8') as names_file:
        for line in names_file:
            cca3 = line[:3]
            country_name = line[3:].strip()
            if cca3 in gdp_data and cca3 in population_data:
                gdp_per_capita.append([country_name, round(gdp_data[cca3] / population_data[cca3], 2)])

    gdp_per_capita.sort(key=lambda x: x[0])

    # Write results to CSV
    with open(out_file_path, 'w', encoding='utf-8', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['Country', 'GDP per Capita'])
        writer.writerows(gdp_per_capita)