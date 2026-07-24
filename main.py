from src.ingestion import fetch_eia_data, save_raw_data

endpoint_crude = "crude_production"
endpoint_natural = "natural_gas"

df_crude = fetch_eia_data(endpoint_crude)
save_raw_data(df_crude, "crpdn_data.csv")

df_natural = fetch_eia_data(endpoint_natural)
save_raw_data(df_natural, "ngsum_data.csv")



print(df_crude.head())
print(df_natural.head())