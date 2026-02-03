import pandas as pd

df = pd.read_csv("leads.csv")

df.drop_duplicates(inplace=True)
df.dropna(subset=["email"], inplace=True)

df["company"] = df["company"].str.title()

df.to_csv("cleaned_leads.csv", index=False)
print("Lead data cleaned.")