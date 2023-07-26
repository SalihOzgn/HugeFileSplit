import pandas as pd
chunks = pd.read_json('sdsf.jsonl', lines=True, chunksize = 500)
for c in chunks:
    print(c)