#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    with open(filename, "r") as file:
        return json.load(file)
