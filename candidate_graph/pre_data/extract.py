import json
import unicodedata as ud


def normalize(str):
    return ud.normalize('NFC', str)

def extractAddress(arr_adress):
    with open('./pre_data.json','a') as f:
        for i in range(len(arr_adress)):
            name_city = normalize(arr_adress[i]["name"].lower()) #city
            district = arr_adress[i]["district"]
            for j in range(len(district)):
                name_dis = normalize(district[j]["name"].lower()) #district
                street = district[j]["street"] #street
                for k in range(len(street)):
                    str = {
                        "street": normalize(street[k]["name"].lower()),
                        "district": name_dis,
                        "city": name_city,
                        "code": arr_adress[i]["code"],
                        "country": "việt nam"
                    }
                    json.dump(str, f, ensure_ascii=False,separators=(',',':'))
                    f.write("\n")
                ward = district[j]["ward"] #ward
                for n in range(len(ward)):
                    war = {
                        "ward": normalize(ward[n]["name"].lower()),
                        "district": name_dis,
                        "city": name_city,
                        "code": arr_adress[i]["code"],
                        "country": "việt nam"
                    }
                    json.dump(war, f, ensure_ascii=False,separators=(',',':'))
                    f.write("\n")

                project = district[j]["project"] #project
                for m in range(len(project)):
                    pro = {
                        "project": normalize(project[m]["name"].lower()),
                        "district": name_dis,
                        "city": name_city,
                        "code": arr_adress[i]["code"],
                        "country": "việt nam",
                        "lat": project[m]["lat"],
                        "lng": project[m]["lng"]
                    }
                    json.dump(pro, f, ensure_ascii=False,separators=(',',':'))
                    f.write("\n")
