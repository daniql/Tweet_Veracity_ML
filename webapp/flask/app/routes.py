from flask import render_template, request, session, url_for
import tensorflow_hub as hub
from app import app, APP_ROOT
import tweepy
import os
from werkzeug.utils import redirect
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

api_key = 'AVbXecczZ8bss5mHJGWhoZfd2'
api_key_secret = 'cTLpvDieSzZPvaaNkhXOQG3nMUln46ycQtEfaYsdSIKSlhF03S'
access_token = '1496715621903618049-g97Xa04OccWl07ernK7b0IsAzk5Eku'
access_token_secret = 'oV3s9zwI1yqJOY6eBWdyvGFQ2EHSf5vr0ry7SrdI0LWo0'

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

@app.route('/')
def home():
    return render_template('predict.html',title='Predict')

@app.route('/anylink')
def anylink():
    pass

@app.route('/predict')
def predict():
    return render_template("home.html",title="Home")


@app.route('/upload',methods=["GET","POST"])
def upload():
    target = os.path.join(APP_ROOT, 'temp/')
    filename = "tweet.txt"
    if request.method == 'POST':
        url = request.form["url"]
        id = url.split("status/",1)[1]
        tweet = api.get_status(id).text
        session['tweet'] = tweet
        return redirect(url_for('.prediction', tweet=tweet))
    return "error"


@app.route("/prediction",methods=["GET", "POST"])
def prediction():
    tweet = request.args['tweet']
    tweet = session['tweet']
    x = classify_tweet(tweet)
    return render_template('output.html', results=x)


class FCNet(nn.Module):
    def __init__(self):
        super(FCNet, self).__init__()
        self.name = "FCNet"
        self.fc1 = nn.Linear(768, 200)
        self.fc2 = nn.Linear(200,20)
        self.fc3 = nn.Linear(20,1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        x = x.squeeze(1)
        return x


def classify_tweet(tweet):
    preproc_url = "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3"
    encoder_url = "https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4"

    bert_preproc_model = hub.KerasLayer(preproc_url)
    bert_encoder_model = hub.KerasLayer(encoder_url)

    net = FCNet()
    model_path = "/Users/danny/Documents/School/APS360/project/webapp/flask/model_FCNet_bs128_lr0.0005_iter1370"
    model_state = torch.load(model_path)
    net.load_state_dict(model_state)

    text_preproc = bert_preproc_model(np.expand_dims(tweet,0))
    bert_res_loc = bert_encoder_model(text_preproc)
    tweet_input = torch.from_numpy(bert_res_loc.numpy())
    output = net(tweet_input)
    prob = torch.sigmoid(output).item()

    if prob >= 0.5:
        return {'true', prob}
    else:
        return {'false', prob}

