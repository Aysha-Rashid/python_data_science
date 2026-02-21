import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_life(file: pd.DataFrame):
    """
    Takes a Dataframe file and sort the values in ascending order,
    finds the country and displays a line chart based on the year
    and the Life expectancy
    """
    try:
        arranged = file.sort_values("country", ascending=True)
        Uae_country = arranged.loc["United Arab Emirates"]
        print("Data of United Arab Emirates")
        print(Uae_country)
        x = Uae_country.index
        y = Uae_country.values
        plt.plot(x, y)
        plt.xticks(x[::40])
        plt.xlabel("Years")
        plt.ylabel("Life Expectancy")
        plt.title("UAE life expandancy Projection")
        plt.show()
    except Exception as e:
        print("Error: ", e)


def main():
    file = load("life_expectancy_years.csv")
    aff_life(file)


if __name__ == "__main__":
    main()
