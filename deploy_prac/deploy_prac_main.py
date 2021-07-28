import tensorflow as tf
import re
import pandas as pd
import os

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, SpatialDropout1D, Embedding,Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
os.chdir('/Users/heechankang/projects/pythonworkspace/git_study/interestings/deploy_prac/archive')

data = pd.read_csv('Sentiment.csv')

data.head()
data.info()
data.describe()
data.shape

data = data[['text', 'sentiment']]

data

def preProcess_data(text):
    text = text.lower()
    new_text = re.sub('[^a-zA-Z0-9\s]', '', text)
    new_text = re.sub('rt', '', new_text)
    return new_text

data['text'] = data['text'].apply(preProcess_data)

data

max_features = 2000

tokenizer = Tokenizer(num_words = max_features, split = ' ')
tokenizer.fit_on_texts(data['text'].values)
X = tokenizer.texts_to_sequences(data['text'].values)
X = pad_sequences(X, 28)

Y = pd.get_dummies(data['sentiment']).values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

embed_dim = 128
lstm_out = 196
batch_size = 512

model = Sequential()
model.add(Embedding(max_features, embed_dim, input_length = X.shape[1]))
model.add(SpatialDropout1D(0.4))
model.add(LSTM(lstm_out, dropout=0.3, recurrent_dropout=0.2, return_sequences=True))
model.add(LSTM(128, recurrent_dropout=0.2))
model.add(Dense(3, activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics='accuracy')

model.fit(X_train, Y_train, epochs=10, batch_size = batch_size, validation_data=(X_test, Y_test))


model.save('sentiment.h5')

