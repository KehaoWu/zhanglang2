import os
import re
import json
import jieba

path = 'result'
outpath = 'result-jieba.txt'
filenames = os.listdir(path)

with open(outpath, 'w') as ofp:
    for filename in filenames:
        filename = os.path.join(path, filename)
        items = json.load(open(filename))
        for item in items:
            sentences = item.get('comment').strip()
            sentences = re.split('。|\n|？', sentences)
            for sentence in sentences:
                words = [word for word in jieba.cut(sentence)]
                words = [re.sub('，|。|《|》|？', '', word) for word in words]
                words = list(filter(lambda item: item != '', words))
                ofp.write(" ".join(words))
                ofp.write('\n')
