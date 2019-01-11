num_lines = 0
with open("../ner_crf/data/data.txt", 'r') as f:
    for line in f:
        num_lines += 1

count = 0
with open("../ner_crf/data/data.txt",'r') as f1:
    with open("../ner_crf/data/train.txt", 'w') as f2:
        with open("../ner_crf/data/test.txt", 'w') as f3:
            for line in f1:
                if(count < 0.67*num_lines):
                    f2.write(line)
                else:
                    f3.write(line)
                count += 1

