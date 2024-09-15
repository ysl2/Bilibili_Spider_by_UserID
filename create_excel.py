import pandas as pd
import json

with open('json/码农高天_245645656/primary/full.json', 'r') as f:
    df = json.load(f)

df = pd.DataFrame(
    df,
    columns=['pub_date', 'title', 'url'],
)

df.to_excel('list.xlsx', index=False)
