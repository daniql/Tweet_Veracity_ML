from difflib import SequenceMatcher
import pandas as pd
import csv

seen = []
clean = []

def high_similarity(seen, line):
    for seen_line in seen:
        if SequenceMatcher(None, seen_line[0], line[0]).ratio() >= 0.75:
            return True

    return False

readfile = '/Users/danny/Documents/School/APS360/project/tweepy/unfiltered/real.csv'
writefile = '/Users/danny/Documents/School/APS360/project/tweepy/filtered/real_fil_75.csv'

with open(readfile, 'r') as in_file, open(writefile, 'w') as out_file:
    datareader = csv.reader(in_file)
    datawriter = csv.writer(out_file)
    for row in datareader:
        if high_similarity(seen, row):
            continue
            
        seen.append(row)
        datawriter.writerow(row)
