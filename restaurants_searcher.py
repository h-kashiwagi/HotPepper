import csv
import json
import requests


#4章APIの構造
"""
APIの構造はpythonの辞書型に似たJSON形式（JavaScript Object Notation）
{
    "customer":{
        "name":"大泉",
        "age": 46
    }
}
サーバーからデータを取得するときや、サーバーとやり取りをするときに使われるため、pythonでも辞書との間で変換しながら使う事が出来る
"""

KEYID = "8c4d3f16aa6fc4c4"
COUNT = 100
PREF = "Z011"
FREEWORD = "渋谷駅"
FORMAT = "json"

PARAMS = {"key": KEYID, 
          "count":COUNT,
          "large_area":PREF, 
          "keyword":FREEWORD, 
          "format":FORMAT
          }


def write_data_to_csv(params):
    restaurants = []
    json_res = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=PARAMS).text #text形式にするメソッド
    response = json.loads(json_res)
    if "error" in response["results"]:
        return print("errorが発生しています") 
    for restaurant in response["results"]["shop"]:
        rest_info = [restaurant["name"], restaurant["open"], restaurant["address"], restaurant["access"]]
        #リストrestaurantにリストを追加していく
        restaurants.append(rest_info)
        #csvファイルを生成
    with open("restaurants_list.csv", "w",newline="") as f: #書き込みモード"w"にすると上書きとなり、元の内容は削除される　*"a"は追記
        writer = csv.writer(f)  #csvファイルの書き込み（出力）
        writer.writerows(restaurants) #writer.writerowだとCSVに書き出した時にデータが縦横ではなく横一行
    return print(restaurants)


        
write_data_to_csv(PARAMS)


#csvで一行空くので行を詰めて出力する方法
#with open("restaurants_list.csv","w",newline="")