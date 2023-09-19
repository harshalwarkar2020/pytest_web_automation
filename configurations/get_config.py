import os
import json


def get_data(product):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(dir_path, 'config.json')
    test_data = {}

    with open(config_file) as json_data:
        extract_data = json.load(json_data)

    test_data = extract_data[product]

    return test_data
