import csv
import matplotlib.pyplot as plt

population_data = {}
out_file_path = 'images/evolution_gdp.png'

def exec(gdp, population, countries):
    # Load GDP data for 2015 and 2022
    gdp_evolution = {}
    with open(gdp, 'r', encoding='utf-8') as gdp_file:
        reader = csv.DictReader(gdp_file)
        for row in reader:
            if int(row['Año']) in range (2015, 2023):
                cca3 = row['CCA3']
                year = int(row['Año'])
                gdp = float(row['PIB ($)'])
                if cca3 not in gdp_evolution:
                    gdp_evolution[cca3] = {}
                gdp_evolution[cca3][year] = gdp

    # Load continent data from population file
    continent_data = {}
    with open(population, 'r', encoding='utf-8') as pop_file:
        reader = csv.DictReader(pop_file)
        for row in reader:
            if 'Continent' in row:
                continent_data[row['CCA3']] = row['Continent']

    # Filter GDP evolution data for South American countries
    south_american_gdp_evolution = {cca3: data for cca3, data in gdp_evolution.items() if continent_data.get(cca3) == 'South America'}

    # Load country names and filter for South America
    south_american_countries = []
    with open(countries, 'r', encoding='utf-8') as names_file:
        for line in names_file:
            cca3 = line[:3]
            country_name = line[3:].strip()
            if cca3 in south_american_gdp_evolution:
                south_american_countries.append((cca3, country_name))

    # Sort by population and select top 7
    top_countries = sorted(south_american_countries, key=lambda x: population_data.get(x[0], 0), reverse=True)[:7]

    # Prepare data for plotting
    years = range(2015, 2023)
    for cca3, country_name in top_countries:
        gdp_values = [gdp_evolution[cca3].get(year, 0) for year in years]
        plt.plot(years, gdp_values, marker='o', label=country_name)

    # Plot configuration
    plt.xlabel('Year')
    plt.ylabel('GDP ($)')
    plt.title('GDP Evolution (2015-2022) in South America')
    plt.legend()
    plt.gcf().set_size_inches(12, 8)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.subplots_adjust(left=0.09, right=0.75)
    plt.grid(True)
    plt.savefig(out_file_path)
