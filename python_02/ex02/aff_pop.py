from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def get_values(row):
    """
        Take an array and return a new array with the values
        as float (replacing human readable format)
    """
    vals = []
    for i in row:
        vals.append(
            float(
                i.replace('k', 'e3')
                .replace('M', 'e6')
            )
        )
    return vals


def aff_pop(file: pd.DataFrame):
    """
        Loads Population total dataset and plots a line graph
        comparing difference in two different countries
    """
    if (file.size == 0):
        raise ValueError("Empyty content")
    Uae_country = file.loc["United Arab Emirates"]
    France = file.loc["France"]
    Uae_country.index = pd.to_numeric(Uae_country.index, errors="coerce")
    France.index = pd.to_numeric(France.index, errors="coerce")
    Uae_country = Uae_country.dropna()
    France = France.dropna()
    Uae_country = Uae_country.loc[(Uae_country.index >= 1800)
                                  & (Uae_country.index <= 2050)]
    France = France.loc[(France.index >= 1800) & (France.index <= 2050)]
    plt.plot(Uae_country.index, get_values(Uae_country.values),
             label="United Arab Emirates", color="blue")
    plt.plot(France.index, get_values(France.values),
             label="France", color="pink")

    def yformatter(x, pos):
        if x >= 1_000_000:
            return f'{int(x/1_000_000)}M'
        if x >= 100_000:
            return f'{int(x/1_000)}k'
        return str(x)
    plt.gca().yaxis.set_major_formatter(yformatter)
    plt.xticks(Uae_country.index[::40])
    plt.yticks([20_000_000, 40_000_000, 60_000_000])
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("Population Projection")
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.show()
    print("Uae data:", Uae_country)
    print("France data:", France)


def main():
    try:
        file = load("population_total.csv")
        aff_pop(file)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
