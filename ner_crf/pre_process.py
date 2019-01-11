with open('../normalize_address_data/city_tag_1', 'r') as f:
    trf = f.read().splitlines()

with open("data_1.txt", "w") as text_file:
    for i in range(len(trf)):
        temp = trf[i].replace(' ', ' O ')
        text_file.write(temp + '\n')
