import nltk
import re
import urllib
import requests

'''
Функция, делающая поиск предложений в google через rapidapi
https://rapidapi.com/apigeek/api/google-search3/endpoints
'''


def search_rapid(query, num=10):
    headers = {
        "x-rapidapi-key": "10572f8cc5msh4b3d78a2b575aebp1b330bjsn409ce92f1100",
        "x-rapidapi-host": "google-search3.p.rapidapi.com"
    }

    query = {
        "q": query,
        "num": num
    }

    resp = requests.get("https://rapidapi.p.rapidapi.com/api/v1/search/" + urllib.parse.urlencode(query),
                        headers=headers)

    results = resp.json()
    return results


'''
Функция, считающая процент от числа
'''


def percentage(count, total, n=1):
    return f"{round(count * 100 / total, n)} %"


'''
Функция, выводящая сообщение в поток стандартного вывода и записывающая его в конец файла 
'''


def print_and_write(text, path):
    text = str(text)

    print(text)

    with open(path, 'a', encoding='utf-8') as f:
        f.write(text + '\n')


'''
Разделение текста на предложения, избавление от лишних пробелов и переходов на новую строку
'''


def tokenize_text(t):
    return [re.sub(r"\s+", " ", sent.strip()) for sent in nltk.sent_tokenize(t.replace("\n", " "))]


'''
Разделение предложения на слова, избавление от лишних символов и чисел;
возвращение мешка слов - множества уникальных слов предложения
'''


def tokenize_sentence(s):
    s = re.sub(r"[^\w]", " ", s)
    s = re.sub(r"[1-9]", " ", s)

    word_list = nltk.word_tokenize(s.lower())
    return set(word_list)


'''
Функция сравнивающая предложение с текстом найденных страниц;
нахождение максимального совпадение
'''


def comparison(words_bag, results):
    maximum = 0
    maximum_link = ''

    for result in results:
        description_words_bag = tokenize_sentence(result['description'])

        score = len(words_bag.intersection(description_words_bag)) / len(words_bag)

        if score > maximum:
            maximum = score
            maximum_link = result['link']

        if maximum == 1.0:
            return maximum, maximum_link

    return maximum, maximum_link
