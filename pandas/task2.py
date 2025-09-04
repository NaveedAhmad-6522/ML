import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("🔍 First 5 rows:")
print(df.head())

print("\n📐 Shape of dataset:")
print(df.shape)

print("\n📋 Column names:")
print(df.columns)

print("\n🧾 Dataset info:")
df.info()

print("\n📊 Summary statistics:")
print(df.describe())