import csv
import json


def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        json_arr = []
        for row in csv_reader:
            json_arr.append(row)

    json_str = json.dumps(json_arr, ensure_ascii=False)
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json_str)


csv_to_json('ads.csv', 'ads.json')
csv_to_json('categories.csv', 'categories.json')
