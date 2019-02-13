var fs = require('fs')
module.exports.extract = function (arr_address){
    for(var i = 0; i < arr_address.length;i++){
         var name_city = arr_address[i]["name"] //city
         var city = arr_address[i]
             var district = city["district"] //district
             for(var k = 0; k < district.length; k++){
                 var name_dis = district[k]["name"]
                 var street = district[k]["street"] //street
                 for( var m = 0; m < street.length;m++){
                        var str = {
                            "street" : street[m]["name"],
                            "district" : name_dis,
                            "city" : name_city,
                            "code" : arr_address[i]["code"],
                            "country" : "Việt Nam"
                        }
                        fs.appendFileSync('./pre_data.json', JSON.stringify(str))
                        fs.appendFileSync('./pre_data.json',"\n")
                 }
                 var ward = district[k]["ward"] //ward
                 for( var n = 0; n < ward.length;n++){
                        var war = {
                            "ward" : ward[n]["name"],
                            "district" : name_dis,
                            "city" : name_city,
                            "code" : arr_address[i]["code"],
                            "country" : "Việt Nam"
                        }
                        fs.appendFileSync('./pre_data.json', JSON.stringify(war))
                        fs.appendFileSync('./pre_data.json',"\n")
                 }
                 var project = district[k]["project"] //project
                 for( var p = 0; p < project.length;p++){
                        var pro = {
                            "project" : project[p]["name"],
                            "district" : name_dis,
                            "city" : name_city,
                            "lat" : project[p]["lat"],
                            "lng" : project[p]["lng"],
                            "code" : arr_address[i]["code"],
                            "country" : "Việt Nam"
                        }
                        fs.appendFileSync('./pre_data.json', JSON.stringify(pro))
                        fs.appendFileSync('./pre_data.json',"\n")
                 }
             }
        }
}