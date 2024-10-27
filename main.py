from scripts import ex1, ex2, ex3, ex4, ex5, ex6
from scripts.constants import countries, gdp, population


def main():
    ex1.exec(gdp, population, countries)
    ex2.exec(population, countries)
    ex3.exec(gdp, population, countries)
    ex4.exec(gdp)
    # ex5.exec()
    # ex6.exec()


if __name__ == '__main__':
    main()
