import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def lifeExpectancyWithGdp(gdp_inflation: pd.DataFrame,
                          life_expectancy_years: pd.DataFrame) -> None:
    """
    Loads GDP per capita and life expectancy datasets and plots
    a scatter graph comparing the two.
    """
    try:
        grossProdAllCountry = gdp_inflation['1900']
        lifeExpendAllCountry = life_expectancy_years['1900']
        plt.scatter(grossProdAllCountry.values, lifeExpendAllCountry.values)
        plt.title("1900", loc="center")
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expentancy")
        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(8))
        plt.show()
    except Exception as e:
        print("Error:", e)
    # The Ticks are the values/magnitude of the x and y axis.
    # Minor ticks are divisions of major ticks.
    # There are two classes Locator and Formatter.
    # Locators determine where the ticks are.


def main():
    long_name = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    gdp_inflation = load(long_name)
    life_expectancy_years = load("life_expectancy_years.csv")
    lifeExpectancyWithGdp(gdp_inflation, life_expectancy_years)


if __name__ == "__main__":
    main()
