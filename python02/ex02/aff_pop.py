import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter
from load_csv import load


def aff_pop(path: str):
    population = load(path)
    population.set_index("country", inplace=True)

    # Extract data for France and Belgium
    p1 = population.loc["France"]
    p2 = population.loc["Belgium"]

    # Convert index to integers and filter years up to 2050
    p1.index = p1.index.astype(int)
    p1 = p1[p1.index <= 2050]  # Filter data up to 2050
    p1_values = p1.str.replace('M', 'e6').str.replace('k', 'e3').astype(float)

    p2.index = p2.index.astype(int)
    p2 = p2[p2.index <= 2050]  # Filter data up to 2050
    p2_values = p2.str.replace('M', 'e6').str.replace('k', 'e3').astype(float)

    plt.figure(figsize=(10, 5))
    plt.plot(p1.index, p1_values, label="France")
    plt.plot(p2.index, p2_values, label="Belgium")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")

    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(40))
    ax.yaxis.set_major_locator(MultipleLocator(20e6))  # Ticks every 20 million

    # Format y-axis to show values like "20M", "40M" instead of 2e7, 4e7
    ax.yaxis.set_major_formatter(FuncFormatter(
        lambda x, _: f"{int(x / 1e6)}M"  # Convert 20,000,000 to "20M"
    ))

    plt.show()
    return
