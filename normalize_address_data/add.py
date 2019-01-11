with open('list_city.txt','r') as f:
    with open('city_tag_2','w') as f1:
        for line in f:
            a = line.split(' ')
            for i in range(len(a)):
                if(i !=len(a)-1 and a[i] != " "):
                    f1.write(a[i] +" "+"THANH_PHO")
                    f1.write("\n")
            f1.write("\n")