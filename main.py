from functions import *
from sys import argv

'''
Открытие файла и чтение, обработка возможных ошибок
'''

formats = ["txt"]

if len(argv) == 1:
    file_path = input(f"Путь к файлу с текстом ({', '.join(formats)}): ")
else:
    file_path = argv[1]

flag = True

while flag:
    try:
        while len(file_path.split('.')) == 0 or file_path.split('.')[-1] not in formats:
            file_path = input("Введите название файла с его расширением: ")

        file_txt = open(file_path, 'r', encoding="utf-8")
        flag = False

    except FileNotFoundError:
        print("Файл не найден!")
        file_path = input("Введите путь к файлу с текстом: ")

try:
    sentences = tokenize_text(file_txt.read())
except UnicodeDecodeError:
    file_txt = open(file_path, 'r')
    sentences = tokenize_text(file_txt.read())

file_txt.close()

'''
Поиск предложений, число уникальных слов в которых, в google;
определение заимствованности предложения в найденных страницах с помощью расстояния Жаккарда
'''

search_results = list()
links = dict()

total = len(sentences)
count = 0

sum_scores = 0
count_scores = 0

print("Поиск предложений в интернете...")
for sentence in sentences:
    words = tokenize_sentence(sentence)

    if len(words) > 7:
        results = (search_rapid(sentence))["results"]

        score, link = comparison(words, results)

        if link not in links:
            links[link] = score
        else:
            links[link] += score

        search_results.append((score, sentence, link))

        sum_scores += score
        count_scores += 1

    count += 1
    if (count / total) // 0.1 > ((count - 1) / total) // 0.1:
        print(percentage(count, total))

print("Поиск успешно завершён!")
print()

'''
Вывод результатов рабоыт программы;
запись в файл с название result_ + название исходного файла в директорию расположения исходного файла
'''

file_path = file_path.split('/')
result_path = '/'.join(file_path[:-1] + [f"result_{''.join((file_path[-1]).split('.')[:-1])}.txt"])

print_and_write("Процент заимствованности текста: " + percentage(sum_scores, count_scores, 2), result_path)

limit_value = 0.9

search_results.sort(reverse=True)
maximum = search_results[0][0]

i = 0
print_and_write("\nНаиболее заимствованные предложения:", result_path)

while i < len(search_results) and search_results[i][0] > maximum * limit_value:
    print_and_write(search_results[i][1], result_path)
    print_and_write(round(search_results[i][0], 4), result_path)

    print_and_write('', result_path)
    i += 1

links = [(links[link], link) for link in links]
links.sort(reverse=True)
maximum = links[0][0]

i = 0
print_and_write("Наиболее используемые ссылки:", result_path)

while i < len(search_results) and links[i][0] > maximum * limit_value:
    print_and_write(links[i][1], result_path)

    print_and_write('', result_path)
    i += 1

print_and_write("Результаты работы по всем предложениям:", result_path)

for search_result in search_results:
    print_and_write(search_result[1], result_path)
    print_and_write(search_result[0], result_path)
    print_and_write(search_result[2], result_path)

    print_and_write('', result_path)
