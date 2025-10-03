import pandas as pd
import chardet

# Function to read CSV files with automatic encoding detection
def read_csv_with_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())  # Detect encoding
    encoding = result['encoding']
    return pd.read_csv(file_path, encoding=encoding)

# Reading the McDonald's dataset with automatic encoding detection
mcdonalds_df = read_csv_with_encoding("data/mcdonalds_dataset_cleaned_without_nodata.csv")

# Function to clean the McDonald's dataset by removing rows containing "Tortilla" in any column
def clean_mcdonalds_dataset(df, common_column):
    # Removing rows containing "Teavana" in any column
    df = df[~df.apply(lambda row: row.astype(str).str.contains('nopost').any(), axis=1)]

    return df

# Cleaning the McDonald's dataset
mcdonalds_df_cleaned = clean_mcdonalds_dataset(mcdonalds_df, "City")

# Saving the cleaned dataset to a new CSV file
mcdonalds_df_cleaned.to_csv("data/mcdonalds_dataset_cleaned_without_nodata2", index=False)
