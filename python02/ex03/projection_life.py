from load_csv import load
import matplotlib.pyplot as plt


def projection():
    expectancy = load("../life_expectancy_years.csv")
    income = load(
        "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )

    year = "1900"

    income = income[year].replace("K", "e3").astype(float)
    life = expectancy[year].astype(float)

    plt.scatter(income, life)
    plt.xscale("log")
    plt.xlabel("Gross domestic product (USD)")
    plt.ylabel("Life Expectancy (years)")
    plt.title(f"{year}")
    plt.show()

    return
