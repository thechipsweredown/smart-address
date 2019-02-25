with open('../pre_data/pre_data.json') as f:
    count = 0
    with open('../data_elasticsearch/data.json',mode='w') as f1:
        for line in f:
            f1.write('{"index":{"_index":"smart_address","_id":'+str(count)+'}'+'}')
            f1.write('\n')
            f1.write(line)
            count += 1
    f1.close
f.close
