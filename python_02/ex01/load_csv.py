import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file and prints its dimensions.
    """
    try:
        if (path.endswith(".csv") is False):
            raise ValueError("Should be a csv file")
        file = pd.read_csv(path, index_col=0)
        data_shape = file.shape
        print("Loading datasets of dimensions", data_shape)
        return (file)
    except Exception as e:
        print("Error:", e)
