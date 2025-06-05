#!/usr/bin/python3

import json
import csv

def convert_csv_to_json(csv_filename):
    try:
        # read csv format file
        with open(csv_filename, "r") as file:
            reader = csv.DictReader(file)  # convert to each row to dictionary
            data = [row for row in reader]

        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)  #serialize (convert to json format)

        return True

    except FileNotFoundError:
        return False
