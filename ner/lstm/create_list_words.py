import pandas as pd
import pickle
data = pd.read_csv("data/train.csv", encoding="utf-8")
data = data.fillna(method="ffill")
words = list(set(data["Word"].values))
words.append("ENDPAD")
tags = list(set(data["Tag"].values))
with open('data/words', 'wb') as f:
    pickle.dump(words, f)
with open('data/tags', 'wb') as f:
    pickle.dump(tags, f)
