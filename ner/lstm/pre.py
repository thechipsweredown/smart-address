import csv
import random

# write array data to csv file
def writeCsv(file, data):
    myFile = open(file, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)
    myFile.close()

with open('../crf/data/test.txt', 'r') as f:
    x = f.readlines()

data = [['Sentence #', 'Word', 'POS', 'Tag']]
sentence = 0
sentence_str, flag = '', False
for i in range(len(x)):
    if x[i] == '\n':
        sentence = sentence + 1
        sentence_str = "Sentence " + str(sentence)
        flag = True
        if i>1:
            data_temp = ['', '.', '.', 'O']
            data.append(data_temp)
    else:
        row = x[i].split((' '))
        word, pos, tag = row[0], row[1], row[2].replace('\n', '')
        if sentence_str != '':
            data_temp = [sentence_str, word, pos, tag]
            sentence_str = ''
        else:
            data_temp = [sentence_str, word, pos, tag]
        data.append(data_temp)
writeCsv('data/test.csv', data)