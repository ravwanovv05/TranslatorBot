import json


def read_json_data(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


def write_json_data(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

