from search import search_rapid

with open("text.txt", "r", encoding='utf-8') as f:
    sentences = (f.readlines()[0]).split(".")

results = []
for sentence in sentences:
    result = search_rapid(sentence.strip())
    result['sentence'] = sentence.strip()
    results.append(result)

print(results)
with open("result.txt", "w", encoding='utf-8') as f:
    f.write(results)
