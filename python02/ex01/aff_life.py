import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from load_csv import load


def aff_life(path: str):
    df = load(path)

    if df is None:
        return

    df.set_index("country", inplace=True)
    data = df.loc["France"]
    data.index = data.index.astype(int)  # Convert index to integers

    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data.values)
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France life expectancy projections")

    # Set x-axis major ticks every 40 years
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(40))

    plt.show()
