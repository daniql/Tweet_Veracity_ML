import pandas as pd
import torchvision
import torch
import numpy as np

# Collect and merge the fake news from the four versions
data1 = pd.read_csv(
    "./CoAID-master/05-01-2020/NewsFakeCOVID-19.csv").to_numpy()
data2 = pd.read_csv(
    "./CoAID-master/07-01-2020/NewsFakeCOVID-19.csv").to_numpy()
data3 = pd.read_csv(
    "./CoAID-master/09-01-2020/NewsFakeCOVID-19.csv").to_numpy()
data4 = pd.read_csv(
    "./CoAID-master/11-01-2020/NewsFakeCOVID-19.csv").to_numpy()
print(data1.shape)
print(data2.shape)
print(data3.shape)
print(data4.shape)
data = np.concatenate((data1, data2, data3, data4))
print(data.shape)  # 925 lines, 15 columns (index included)

# Convert all values in str
data = data.astype(str)

############################################################################

# What different values we have in the columns ?

# First column : type
#print(np.unique(data[:, 1], return_counts=True))
# # 673 'posts', 212 'articles', 40 'nan'

# Second column : fact_check_url
#print(np.unique(data[:, 2], return_counts=True))
# no 'nan'

# Third column : archive
#print(np.unique(data[:, 3], return_counts=True))
# 548 'nan'

# Fourth column : news_url
#print(np.unique(data[:, 4], return_counts=True))
# 40 'nan'

# Fifth column : news_url2
#print(np.unique(data[:, 5], return_counts=True))
# 832 'nan'

# Sixth column : news_url3
#print(np.unique(data[:, 6], return_counts=True))
# 865 'nan'

# Seventh column : news_url4
#print(np.unique(data[:, 7], return_counts=True))
# 891 'nan'

# Eighth column : news_url5
#print(np.unique(data[:, 8], return_counts=True))
# 910 'nan'

# Ninth column: title
#print(np.unique(data[:, 9],return_counts=True))
# Ò at the beginning and at the end sometimes, sometimes in the middle

# Tenth column: news_title
#print(np.unique(data[:, 10], return_counts=True))
# 458 'nan', 32 "", repeated values, sometimes the author ? --> I don't think it is meaningful

# Eleventh column: content
#print(np.unique(data[:, 11], return_counts=True))
# 509 'nan', 20 'you must log in to continue.. ', things like 'confirm to receive notifications', 'do you want to join facebook?', 'see more of ... on facebook'

# Twelfth column: abstract
#print(np.unique(data[:, 12], return_counts=True))
# 656 'nan'

# Thirteenth column: publish_date
#print(np.unique(data[:, 13], return_counts=True))
# 780 'nan' + different formats of date

# Fourteenth column: meta_keywords
#print(np.unique(data[:, 14], return_counts=True))
# 458 'nan', 405 '""'
