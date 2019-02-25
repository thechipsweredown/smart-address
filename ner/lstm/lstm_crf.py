from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
from keras.models import Model, Input
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from keras_contrib.layers import CRF
import pickle
data = pd.read_csv("data/train.csv", encoding="utf-8")
data = data.fillna(method="ffill")
words = []
tags = []
with open('data/words', 'rb') as f:
    words = pickle.load(f)
with open('data/tags', 'rb') as f:
    tags = pickle.load(f)
n_words = len(words)
n_tags = len(tags)
max_len=75

def create_model():
    input = Input(shape=(max_len,))
    model = Embedding(input_dim=n_words + 1, output_dim=20,
                      input_length=max_len, mask_zero=True)(input)  # 20-dim embedding
    model = Bidirectional(LSTM(units=50, return_sequences=True,
                               recurrent_dropout=0.1))(model)  # variational biLSTM
    model = TimeDistributed(Dense(50, activation="relu"))(model)  # a dense layer as suggested by neuralNer
    crf = CRF(n_tags)  # CRF layer
    out = crf(model)  # output

    model = Model(input, out)
    model.compile(optimizer="rmsprop", loss=crf.loss_function, metrics=[crf.accuracy])
    return model

model = create_model()
model.load_weights('model/lstm_crf.h5')
text="đại cồ việt, hai bà trưng, hà nội"
test_sentence = text.split(' ')
temp = []
for i in test_sentence:
    if "," not in i:
        temp.append(i.capitalize())
    else:
        temp.append(i.replace(",", "").capitalize())
        temp.append(",")
word2idx = {w: i + 1 for i, w in enumerate(words)}
x_test_sent = pad_sequences(sequences=[[word2idx.get(w, 0) for w in temp]],
padding="post", value=0, maxlen=75)
p = model.predict(np.array([x_test_sent[0]]))
p = np.argmax(p, axis=-1)
print("{:15}||{}".format("Word", "Prediction"))
print(30 * "=")
for w, pred in zip(temp, p[0]):
    print("{:15}: {:5}".format(w, tags[pred]))