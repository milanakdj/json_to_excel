import json

import pandas as pd

FILE_NAME = "list3.json"
OUTPUT_NAME = FILE_NAME.split(".")[0]


def load_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

def convert_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel(f'{OUTPUT_NAME}.xlsx', index=False)
    return df

def convert(steps):
    for i, step in enumerate(steps):
        if i ==0:
            filename = FILE_NAME
            data = step(filename)
        else:
            data = step(data)   
    return data


if __name__== "__main__":
    steps = [load_json, convert_to_excel] #uses the global FILE_NAME, and OUTPUT_NAME
    data = convert(steps)
    print(data)


