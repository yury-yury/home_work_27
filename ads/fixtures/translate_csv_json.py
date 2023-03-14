import csv
import json


def csv_to_json(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        json_arr = []
        for row in csv_reader:
            json_arr.append(row)

    return json_arr


json_list = []
list_ads = csv_to_json('ads.csv')
for row in list_ads:
    json_list.append({
        "model": "ads.ads",
        "pk": int(row["Id"]),
        "fields": {
            "name": row["name"],
            "author": row["author"],
            "price": int(row["price"]),
            "description": row["description"],
            "address": row["address"],
            "is_published": row["is_published"]}})

list_category = csv_to_json('categories.csv')
for row in list_category:
    json_list.append({
        "model": "ads.category",
        "pk": int(row["id"]),
        "fields": {
            "name": row["name"]}})

json_str = json.dumps(json_list, ensure_ascii=False)
with open('ads.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json_str)