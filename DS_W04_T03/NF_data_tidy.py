import pandas as pd 

file_path='DS_W04_T03/data/Netflix_Data.csv'

# Read the CSV file into a DataFrame
try:
    df=pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit()

# 1. Count the number of samples
num_samples = len(df)-1

# 2. Count and list out features
num_features = df.shape[1]
feature_list = df.columns.tolist()

# 3. Count Null/Missing Values
missing_values_count=df.isnull().sum()

# 4. Datatype of each column
data_types=df.dtypes

# 5. Total numbers of Samples and Features
print("\n--- Advanced Python (Pandas) Analysis ---")
print(f"1. **Number of Samples:** {num_samples}")
print(f"2. **Number of Features:** {num_features}")
print(f"   **Feature List:** {feature_list}")

# Missing Values
print("\n3. **Missing Values Count:** (Pandas recognizes 'NaN' from blank cells)")
print(missing_values_count)

# List of the missing/null values' position
# Give the "date_added" for example
print()
show_id_column=df['show_id'].to_list()
date_added_column=df['date_added'].to_list()
for index, value in enumerate(date_added_column):
    if pd.isna(value):
        print(f'\t-- Null value of date added found at {show_id_column[index]}')

print("\n4. **Column Datatypes (Dtypes):** (Automatically inferred)")
print(data_types)

# Display a snapshot
print("\n**Data Snapshot (First 5 rows):**")
print(df.head())