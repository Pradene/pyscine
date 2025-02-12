import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Read a CSV file, print the dimensions of the dataset, first few rows.
    Handles errors for missing files, empty files, and invalid formats.

    :param path: Path to the CSV file
    :return: Pandas DataFrame
    """
    try:
        df = pd.read_csv(path)

        # Handle empty dataset
        if df.empty:
            print("Warning: The dataset is empty.")
            return df

        print(f"Loading dataset of dimensions {df.shape}")
        print(df.head())

        return df

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return None

    except pd.errors.EmptyDataError:
        print(f"Error: The file '{path}' is empty.")
        return None

    except pd.errors.ParserError:
        print(f"Error: The file '{path}' is not a valid CSV format.")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
