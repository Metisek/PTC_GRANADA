import csv
import re
import matplotlib.pyplot as plt

out_file_path = 'images/evolution_population.png'


def exec(population):
    continent_population_by_year = {}

    with open(population, 'r', encoding='utf-8') as pop_file:
        reader = csv.DictReader(pop_file)
        for row in reader:
            continent = row['Continent']
            if continent not in ['Asia', 'North America', 'Europe']:
                continue

            for key, value in row.items():
                match = re.match(r'(\d{4}) Population', key)
                if match:
                    year = match.group(1)
                    population_count = int(value)

                    if year not in continent_population_by_year:
                        continent_population_by_year[year] = {'Asia': 0, 'North America': 0, 'Europe': 0}

                    continent_population_by_year[year][continent] += population_count

    years = sorted(continent_population_by_year.keys())
    asia_population = [continent_population_by_year[year]['Asia'] for year in years]
    north_america_population = [continent_population_by_year[year]['North America'] for year in years]
    europe_population = [continent_population_by_year[year]['Europe'] for year in years]

    plt.figure(figsize=(12, 8))
    index = range(len(years))
    bar_width = 0.25

    plt.bar([i - bar_width for i in index], asia_population, width=bar_width, label='Asia')
    plt.bar(index, north_america_population, width=bar_width, label='North America')
    plt.bar([i + bar_width for i in index], europe_population, width=bar_width, label='Europe')

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Evolution by Continent')
    plt.xticks(index, years, rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.legend()
    plt.savefig(out_file_path)
    plt.close()
