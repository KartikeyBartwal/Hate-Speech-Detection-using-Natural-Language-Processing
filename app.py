import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import tensorflow
import keras
import re
import pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
stopword=set(stopwords.words('english'))
import string
stemmer = nltk.SnowballStemmer("english")



with open('hate_speech_detection_model.pkl', 'rb') as file:
    model = pickle.load(file)
    file.close()
with open('count_vectorizer.pkl', 'rb') as file:
    count = pickle.load(file)
    file.close()


def engineer_text(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text


def use_model(text):
    text = [engineer_text(text)]
    seq = count.transform(text)
    print(text)
    print()
    print(seq)
    print()
    
    output = model.predict(seq)
    print(output)
    
    if(output >= 0 and output <= 1.88 and output != 1.77):
        return "Hate and offensive speech"
    else:
        return "Safe Speech"


from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask("hate_speech_detection_model")


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/result", methods = ["POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        text = request.form.get("input_text")
        res = use_model(text)
        print(res)
        return render_template('home.html',result=res)
    else:
        return render_template("home.html")
