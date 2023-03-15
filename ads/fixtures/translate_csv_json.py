import csv
import json


def csv_to_dict(csv_file: str) -> list:
    """
    The csv_to_dict function takes as an argument the name and location of a file with data in CSV format
    as a string. When called, it opens a file for reading, reads data and converts it into a dictionary
    in python format. Returns the resulting dictionary in python format.
    """
    with open(csv_file, 'r', encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        json_arr: list = []
        for row in csv_reader:
            json_arr.append(row)

    return json_arr


def write_json(json_list: list) -> None:
    """
    The write_json function takes as an argument a dictionary in the format necessary to form the initial values
    of the database in the form of a dictionary. When called, it converts the dictionary to JSON format,
    opens a file for writing and writes data to a file in JSON format.
    """
    json_str: str = json.dumps(json_list, ensure_ascii=False)
    with open('ads.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json_str)


json_list: list = []
list_ads: list = csv_to_dict('ads.csv')
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

list_category: list = csv_to_dict('categories.csv')
for row in list_category:
    json_list.append({
        "model": "ads.category",
        "pk": int(row["id"]),
        "fields": {
            "name": row["name"]}})

write_json(list_category)
