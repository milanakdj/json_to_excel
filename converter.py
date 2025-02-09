import json

import pandas as pd

with open("list.json", "r") as file:
    data = json.load(file)

# print(data)
json_str = json.dumps(data, indent=4)

# Print the pretty-printed JSON string
# print(json_str)
df = pd.DataFrame(data)
print(df)


df.to_excel('output.xlsx', index=False)

