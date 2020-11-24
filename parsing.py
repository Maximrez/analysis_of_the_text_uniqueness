from search import search_rapid
from norm_and_uniq import search_normalize, non_uniqueness

PATH_DIR = "data/"
FILE_NAME = "new"

with open(PATH_DIR+"text_"+FILE_NAME+".txt", "r", encoding='utf-8') as f:
    sentences = (f.readline()).split(".")

results = []
for sentence in sentences:
    if len(sentence.split()) < 5:
        continue
    result = search_rapid(sentence.strip())
    result['sentence'] = sentence.strip()
    results.append(result)

results = search_normalize(results)
print(results)

with open(PATH_DIR+"searches_"+FILE_NAME+".txt", "w", encoding='utf-8') as f:
    f.write(str(results))

non_uniqueness(results, PATH_DIR+"result_"+FILE_NAME+".txt")