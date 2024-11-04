import requests
import csv

def fetch_countries_and_capitals():
    url = "https://restcountries.com/v3.1/region/europe"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

def write_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Country", "Capital"])
        for country in data:
            country_name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0]
            writer.writerow([country_name, capital])

def main():
    data = fetch_countries_and_capitals()
    write_to_csv(data, 'capitals.csv')

if __name__ == "__main__":
    main()