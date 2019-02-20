import pycrfsuite

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
def get_map_entity(pred):
    number = []
    street = []
    ward = []
    dist = []
    city = []
    for i in range(len(pred)):
        if pred[i][1].endswith("NUMBER"):
            number.append(pred[i][0].lower())
        if pred[i][1].endswith("STREET"):
            street.append(pred[i][0].lower())
        if pred[i][1].endswith("WARD"):
            ward.append(pred[i][0].lower())
        if pred[i][1].endswith("DIST"):
            dist.append(pred[i][0].lower())
        if pred[i][1].endswith("CITY"):
            city.append(pred[i][0].lower())
    map = {}
    map["number"] = " ".join(number)
    map["street"] = " ".join(street)
    map["ward"] = " ".join(ward)
    map["dist"] = " ".join(dist)
    map["city"] = " ".join(city)
    return map

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
    tagger.open('../../ner_crf/model/crf.model')
    y_detect = [tagger.tag(xseq) for xseq in X_detect]
    pred = []
    for i in range(len(temp)):
        k = temp[i]
        v = y_detect[0][i]
        kv = []
        kv.append(k)
        kv.append(v)
        pred.append(tuple(kv))
    return get_map_entity(pred)

