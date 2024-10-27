import csv

out_file_path = 'csv_out/gdp_growth.csv'

def exec(gdp):

    # Calculate GDP growth rates for countries with CCA3 starting with 'D' or 'E'
    growth_rates = []
    with open(gdp, 'r', encoding='utf-8') as gdp_file:
        reader = csv.DictReader(gdp_file)
        gdp_evolution = {}
        for row in reader:
            if int(row['Año']) in range(2018, 2023):
                cca3 = row['CCA3']
                year = int(row['Año'])
                gdp = float(row['PIB ($)'])
                if cca3 not in gdp_evolution:
                    gdp_evolution[cca3] = {}
                gdp_evolution[cca3][year] = gdp

    for cca3, data in gdp_evolution.items():
        if cca3.startswith('D') or cca3.startswith('E'):
            growth_rate = {}
            for year in range(2018, 2023):
                if year in data and (year - 1) in data:
                    previous_gdp = data[year - 1]
                    current_gdp = data[year]
                    growth_rate[year] = round(((current_gdp - previous_gdp) / previous_gdp) * 100, 2)
            if growth_rate:
                growth_rates.append({'CCA3': cca3, **growth_rate})

    # Sort growth rates by CCA3
    growth_rates.sort(key=lambda x: x['CCA3'])

    # Write growth rates to CSV file
    with open(out_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['CCA3'] + [year for year in range(2019, 2023)]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in growth_rates:
            writer.writerow(row)