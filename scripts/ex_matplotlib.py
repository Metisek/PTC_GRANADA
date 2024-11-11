import csv
import matplotlib.pyplot as plt
import re

# Define the file paths
population_file = 'data/world_population.csv'
output_file_path = 'images/matplotlib_defensa.png'


def exec(population_file):
    largest_european_countries = get_largest_european_countries(population_file)
    population_data = load_population_data(population_file, largest_european_countries)
    plot_population_density(population_data)

def get_largest_european_countries(population_file, continent='Europe', top_n=3):
    countries_by_area = []
    with open(population_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Continent'] == continent and 'Area (km²)' in row:
                try:
                    area = float(row['Area (km²)'])
                    countries_by_area.append((row['CCA3'], area))
                except ValueError:
                    continue
    # Sort by area and get the top N largest countries
    largest_countries = sorted(countries_by_area, key=lambda x: x[1], reverse=True)[:top_n]
    return largest_countries

def load_population_data(population_file, countries):
    population_data = {country: {'area':area} for country, area in countries}
    all_countries = [country for country, _ in countries]
    with open(population_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cca3 = row['CCA3']
            if cca3 in all_countries:
                for key, value in row.items():
                    match = re.match(r'(\d{4}) Population', key)
                    if match:
                        year = int(match.group(1))
                        population_data[cca3][year] = int(value) / population_data[cca3]['area']
    return population_data

def plot_population_density(data):
    # Plot each country's population density over time
    for cca3, yearly_data in data.items():
        years = sorted(year for year in yearly_data.keys() if year != 'area')
        densities = [yearly_data[year] for year in years]
        plt.plot(years, densities, label=cca3)

    # Configure plot
    plt.xlabel('Año')
    plt.ylabel('Densidad de Población')
    plt.title('Evolución de densidad de población')
    plt.legend(title="País")
    plt.grid(True)
    plt.savefig(output_file_path)
    plt.close()
