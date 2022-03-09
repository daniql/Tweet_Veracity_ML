import pandas as pd
import numpy as np

df_fake = pd.read_csv('/Users/danny/Documents/School/APS360/project/tweepy/filtered/fake_fil_75.csv', header=None)
df_real = pd.read_csv('/Users/danny/Documents/School/APS360/project/tweepy/filtered/real_fil_75.csv', header=None)

df_fake.columns = ["Text", "Label"]
df_real.columns = ["Text", "Label"]

df_comb = df_fake.append(df_real)
df_shuffled = df_comb.sample(frac=1)
df_shuffled = df_shuffled.reset_index(drop=True)
print(df_shuffled)

df_shuffled.to_csv('/Users/danny/Documents/School/APS360/project/tweepy/filtered/db_75.csv', encoding='utf-8')
