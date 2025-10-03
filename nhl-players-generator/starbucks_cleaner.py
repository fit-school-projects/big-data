import pandas as pd
import chardet

# Funkcia na načítanie CSV súborov s automatickým rozpoznávaním kódovania
def read_csv_with_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())  # Detekcia kódovania
    encoding = result['encoding']
    return pd.read_csv(file_path, encoding=encoding)

# Načítanie datasetu Starbucks s automatickým rozpoznávaním kódovania
starbucks_df = read_csv_with_encoding("data/starbucks_dataset_cleaned.csv")

# Funkcia na odstránenie nulových hodnôt a riadkov s hodnotou v stĺpci "City" začínajúcou na otáznik (?)
def clean_starbucks_dataset(df, common_column):
    # Odstránenie nulových hodnôt
    # df = df.dropna()
    # df = df[df['Brand'] == 'Starbucks']
    # Odstránenie riadkov s hodnotou v stĺpci "City" začínajúcou na otáznik (?)
    df = df[~df['Postcode'].str.startswith('nopost')]
    # Odstránenie nevyužitých stĺpcov
    # columns_to_keep = [common_column] + [col for col in df.columns if col != common_column]
    # df = df[columns_to_keep]
    return df

# Odstránenie nulových hodnôt, nežiadúcich hodnôt v stĺpci "City" a nevyužitých stĺpcov pre dataset Starbucks
starbucks_df_cleaned = clean_starbucks_dataset(starbucks_df, "City")

# Uloženie upraveného datasetu do nového CSV súboru
starbucks_df_cleaned.to_csv("data/starbucks_dataset_cleaned.csv", index=False)
