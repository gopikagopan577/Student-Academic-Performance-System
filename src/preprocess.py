import pandas as pd


df = pd.read_csv('Data/Processed_data.csv')


print(df.head())
print("Shape:", df.shape)


X = df.drop(columns=['final_grade'])
y = df["final_grade"]


print('Input features:')
print(X.columns)

print('Target:')
print(y.name)

print('X shape:', X.shape)
print('y shape:', y.shape)