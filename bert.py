import tensorflow_hub as hub
import tensorflow_text as text
import pandas as pd
import numpy as np

preproc_url = "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3"
encoder_url = "https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4"

bert_preproc_model = hub.KerasLayer(preproc_url)
bert_encoder_model = hub.KerasLayer(encoder_url)


data1 = pd.read_csv(
    "./CoAID-master/05-01-2020/NewsFakeCOVID-19.csv").to_numpy()
data2 = pd.read_csv(
    "./CoAID-master/07-01-2020/NewsFakeCOVID-19.csv").to_numpy()
data3 = pd.read_csv(
    "./CoAID-master/09-01-2020/NewsFakeCOVID-19.csv").to_numpy()
data4 = pd.read_csv(
    "./CoAID-master/11-01-2020/NewsFakeCOVID-19.csv").to_numpy()
data = np.concatenate((data1, data2, data3, data4))
# Select the column titles
titles = list(data[:, 9])

text_preproc = bert_preproc_model(titles)
bert_res = bert_encoder_model(text_preproc)['pooled_output']
print(bert_res)
