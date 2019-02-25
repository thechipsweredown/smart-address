import pickle
import sklearn_crfsuite
import pycrfsuite
from sklearn_crfsuite import metrics
def write(data, outfile):
    f = open(outfile, "w+b")
    pickle.dump(data, f)
    f.close()

with open('data/train.txt', 'r') as f:
    trf = f.read().splitlines()

with open('data/test.txt', 'r') as f1:
    tef = f1.read().splitlines()

ls = []
arr = []

ls_test = []
arr_test = []

for i in range(len(trf)):
    if trf[i] != "":
        a = trf[i].split(' ')
        if len(a) != 3:
            print(a[0] + " " + a[1])
        ls.append(tuple(a))
arr.append(ls)

train_sents = arr

for i in range(len(tef)):
    if tef[i] != "":
        a = tef[i].split(' ')
        if len(a) != 3:
            print(a[0] + " " + a[1])
        ls_test.append(tuple(a))
arr_test.append(ls_test)

train_sents = arr
test_sents = arr_test

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


def extract_features(doc):
    return [word2features(doc, i) for i in range(len(doc))]

# A function fo generating the list of labels for each document
def get_labels(doc):
    return [label for (token, postag, label) in doc]

X_train = [extract_features(doc) for doc in train_sents]
y_train = [get_labels(doc) for doc in train_sents]

X_test = [extract_features(doc) for doc in test_sents]
Y_test = [get_labels(doc) for doc in test_sents]



crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True
)
crf.fit(X_train, y_train)

labels = list(crf.classes_)
labels.remove('OTHER')

trainer = pycrfsuite.Trainer(verbose=True)

# Submit training data to the trainer
for xseq, yseq in zip(X_train, y_train):
    trainer.append(xseq, yseq)

# Set the parameters of the model
trainer.set_params({
    # coefficient for L1 penalty
    'c1': 0.1,

    # coefficient for L2 penalty
    'c2': 0.01,

    # maximum number of iterations
    'max_iterations': 200,

    # whether to include transitions that
    # are possible, but not observed
    'feature.possible_transitions': True
})

# Provide a file name as a parameter to the train function, such that
# the model will be saved to the file when training is finished
trainer.train('model/crf.model')
tagger = pycrfsuite.Tagger()
tagger.open('model/crf.model')

#Tag
Y_pred = crf.predict(X_test)
from seqeval.metrics import precision_score, recall_score, f1_score, classification_report
print("F1-score: {:.1%}".format(f1_score(Y_test, Y_pred)))
print(classification_report(Y_test, Y_pred))

# #Accurancy
# Y_pred = crf.predict(X_test)
# print(metrics.flat_f1_score(Y_test, Y_pred,
#                       average='weighted', labels=labels))
# sorted_labels = sorted(
#     labels,
#     key=lambda name: (name[1:], name[0])
# )
# print(metrics.flat_classification_report(
#     Y_test, Y_pred, labels=sorted_labels, digits=3
# ))

