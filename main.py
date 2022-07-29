import yaml
import requests


HTTP = 'http://127.0.0.1:8000/mapping/'
YML_NAME = 'shops.yml'


def parsing_inverse(file_name):
    result = []
    with open(file_name, encoding="utf8") as file:
        my_list = yaml.safe_load(file)
        for name in my_list.keys():
            for value in my_list[name].keys():
                for key in my_list[name][value]:
                    result.append({'name': name, 'key': key, 'value': value})
    return result


if __name__ == "__main__":
    parsing_inverse(YML_NAME)
    for data in parsing_inverse(YML_NAME):
        response = requests.post(HTTP, json=data)
