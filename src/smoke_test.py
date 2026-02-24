import pandas as pd
import pathlib

# Get repo root (folder above 'src')
repo_root = pathlib.Path(__file__).parent.parent

# Path to CSV file
csv_path = repo_root / "data" / "sample.csv"

# Load data
df = pd.read_csv(csv_path)

# Print required outputs
print("Shape:", df.shape)
print("\nHead:")
print(df.head())

print("\nDescribe:")
print(df.describe())