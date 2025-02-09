import json

import pandas as pd

FILE_NAME = "list3.json"
OUTPUT_NAME = FILE_NAME.split(".")[0]

with open(FILE_NAME, "r") as file:
    data = json.load(file)

# print(data)
json_str = json.dumps(data, indent=4)

# Print the pretty-printed JSON string
# print(json_str)
df = pd.DataFrame(data)
print(df)


df.to_excel(f'{OUTPUT_NAME}.xlsx', index=False)

