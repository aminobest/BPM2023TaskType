import json
import pandas as pd


def read_json(path):
    with open(path, encoding='utf-8') as inFile:
        return json.load(inFile)


