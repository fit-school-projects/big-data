import pandas as pd
import chardet


# Funkcia na načítanie CSV súborov s automatickým rozpoznávaním kódovania
def read_csv_with_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())  # Detekcia kódovania
    encoding = result['encoding']
    return pd.read_csv(file_path, encoding=encoding)


# Načítanie datasetov s automatickým rozpoznaním kódovania
mcdonalds_df = read_csv_with_encoding("data/mcdonalds_dataset.csv")
starbucks_df = read_csv_with_encoding("data/starbucks_dataset.csv")
health_city_df = read_csv_with_encoding("data/healthy_lifestyle_data.csv")


# Funkcia na odstránenie nulových hodnôt a nevyužitých stĺpcov
def clean_dataset(df, common_column):
    # Odstránenie nulových hodnôt
    df = df.dropna()
    # Odstránenie nevyužitých stĺpcov
    columns_to_keep = [common_column] + [col for col in df.columns if col != common_column]
    df = df[columns_to_keep]
    return df


# Odstránenie nulových hodnôt a nevyužitých stĺpcov pre každý dataset
mcdonalds_df_cleaned = clean_dataset(mcdonalds_df, "city")
starbucks_df_cleaned = clean_dataset(starbucks_df, "City")
health_city_df_cleaned = clean_dataset(health_city_df, "City")

# Uloženie upravených datasetov do nových CSV súborov
mcdonalds_df_cleaned.to_csv("data/mcdonalds_dataset_cleaned.csv", index=False)
starbucks_df_cleaned.to_csv("data/starbucks_dataset_cleaned.csv", index=False)
health_city_df_cleaned.to_csv("data/healthy_lifestyle_dataset_cleaned.csv", index=False)
