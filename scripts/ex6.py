import csv
import matplotlib.pyplot as plt

population_area_data = {}
out_file_path = 'images/density_continents.png'

def exec(population):

    # Load population and area data with country codes and continent
    with open(population, 'r', encoding='utf-8') as pop_file:
        reader = csv.DictReader(pop_file)
        for row in reader:
            cca3 = row['CCA3']
            population_area_data[cca3] = {
                'population': int(row['2022 Population']),
                'area': float(row['Area (km²)']),
                'continent': row['Continent']
            }

    # Compute density
    continent_density = {}
    for cca3, data in population_area_data.items():
        continent = data['continent']
        area = data['area']
        if continent not in continent_density:
            continent_density[continent] = []
        continent_density[continent].append([data['population'], area])

    # Compute sum of population and areas
    continent_population_area = {}
    for continent, values in continent_density.items():
        population_sum = sum([population for population, _ in values])
        area_sum = sum([area for _, area in values])
        continent_population_area[continent] = (population_sum, area_sum)

    # Compute density
    continent_density = {}
    for continent, (population_sum, area_sum) in continent_population_area.items():
        continent_density[continent] = population_sum / area_sum

    # Sort data by density
    continent_density = dict(sorted(continent_density.items(), key=lambda x: x[1], reverse=True))

    # Prepare data for plotting
    continents = list(continent_density.keys())
    avg_densities = [continent_density[continent] for continent in continents]

    # Create horizontal bar chart
    plt.figure(figsize=(10, 6))
    colors = plt.cm.tab10(range(len(continents)))
    bars = plt.barh(continents, avg_densities, color=colors)
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width():.2f}', va='center')
    plt.xlim(right=max(avg_densities) * 1.1)  # Increase the x-axis limit by 10% to add space on the right
    plt.xlabel('Average Population Density (people per km²)')
    plt.title('Average Population Density by Continent')
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest density on top
    plt.tight_layout()

    # Save the plot
    plt.savefig(out_file_path)
    plt.close()