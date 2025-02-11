import pandas

def load(path: str) -> pandas.DataFrame:
	"""
	Read a csv file and print the dimension of the dataset and first rows
	return the dataset
	"""

	ds = pandas.read_csv(path)
	print(f"Loading dataset of dimensions {ds.shape}")
	print(ds.head())

	return ds