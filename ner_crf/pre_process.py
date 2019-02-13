with open('raw-data/data_old.txt', 'r') as f:
    trf = f.read().splitlines()

with open("raw-data/data_3.txt", "w") as text_file:
    for i in range(len(trf)):
        temp = trf[i].replace(' ', ' O ')
        text_file.write(temp + '\n')
