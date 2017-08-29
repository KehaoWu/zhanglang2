from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('corpus.bin', binary=True)

res = model.most_similar("战狼")
print(res)

res = model.most_similar(positive=["战狼", "吴京"])
print(res)

res = model.most_similar(positive=["战狼", "导演"])
print(res)

res = model.most_similar(positive=["吴京", "演技"])
print(res)
