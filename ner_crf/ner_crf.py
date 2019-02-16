import pycrfsuite
from pyvi import ViTokenizer, ViPosTagger

def word2features(sent, i):
    word = sent[i][0]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
    }
    if i > 0:
        word1 = sent[i-1][0]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
        })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]

def detect_entity(address):
    temp = []
    for i in address.split(" "):
        if "," not in i:
            temp.append(i)
        else :
            temp.append(i.replace(",",""))
            temp.append(",")
    detect = []
    for j in temp:
        l = []
        l.append(j)
        l.append("O")
        detect.append(tuple(l))
    arr = []
    arr.append(detect)
    X_detect = [sent2features(s) for s in arr]
    tagger = pycrfsuite.Tagger()
    tagger.open('model/crf.model')
    y_detect = [tagger.tag(xseq) for xseq in X_detect]
    print(y_detect)
    pred = []
    for i in range(len(temp)):
        k = temp[i]
        v = y_detect[0][i]
        kv = []
        kv.append(k)
        kv.append(v)
        pred.append(tuple(kv))
    return pred
address = "Đại Cồ Việt, Hai Bà Trưng, Hà Nội"
entity = detect_entity(address)

print(entity)
print("Hà Nội" == "Hà Nội")