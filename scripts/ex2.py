import csv
import re

# Load data from files
population_area_data = {}
out_file_path = 'csv_out/density_population_europe.csv'


def exec(population, countries):
    with open(population, 'r', encoding='utf-8') as pop_file:
        reader = csv.DictReader(pop_file)
        for row in reader:
            cca3 = row['CCA3']
            population_area_data[cca3] = {
                'population': {},
                'area': float(row['Area (km²)'])
            }

            for key in row.keys():
                match = re.match(r'(\d{4}) Population', key)
                if match:
                    year = match.group(1)
                    population_area_data[cca3]['population'][year] = int(re.sub(r'[^\d]', '', row[key]))

            # Sort the population data by year
            population_area_data[cca3]['population'] = dict(sorted(population_area_data[cca3]['population'].items()))

    # Get the population density for each country
    countries_with_density = []
    with open(countries, 'r', encoding='utf-8') as names_file:
        for line in names_file:
            cca3 = line[:3]
            country_name = line[3:].strip()
            if cca3 in population_area_data:
                densities = [round(population_val / population_area_data[cca3]['area'], 4) for _, population_val in population_area_data[cca3]['population'].items()]
                countries_with_density.append([country_name] + densities)

    # Sort countries with density by country name
    countries_with_density.sort(key=lambda x: x[0])

    # Write results to CSV
    with open(out_file_path, 'w', encoding='utf-8', newline='') as out_file:
        writer = csv.writer(out_file)
        # Create header
        header = ['Country']
        years = sorted({year for cca3 in population_area_data for year in population_area_data[cca3]['population'].keys()})
        header.extend([f"{year} dens." for year in years])
        writer.writerow(header)

        # Write data
        for country_data in countries_with_density:
            writer.writerow(country_data)