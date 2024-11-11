from scripts import ex1, ex2, ex3, ex4, ex5, ex6, ex_numpy, ex_matplotlib
from scripts.constants import countries, gdp, population


def main():
    ex1.exec(gdp, population, countries)
    ex2.exec(population, countries)
    ex3.exec(gdp, population, countries)
    ex4.exec(gdp)
    ex5.exec(population)
    ex6.exec(population)
    ex_numpy.exec(gdp, countries)
    ex_matplotlib.exec(population)

if __name__ == '__main__':
    main()
