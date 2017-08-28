import os
import json

path = 'result'
outpath = 'result.txt'
filenames = os.listdir(path)

with open(outpath, 'w') as ofp:
    for filename in filenames:
        filename = os.path.join(path, filename)
        items = json.load(open(filename))
        for item in items:
            ofp.write(item.get('comment').strip())
