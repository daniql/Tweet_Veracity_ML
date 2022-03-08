import os
import glob 
import pandas as pd

os.chdir("/Users/danny/Documents/School/APS360/Project/tweepy/processed")

extension  = 'csv'
all_filename = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filename])
combined_csv.to_csv("real.csv", index=False, encoding='utf-8-sig')