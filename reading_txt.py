import codecs

path = 'text.txt'  # path - путь к текстовому файлу
file = codecs.open(path, encoding='utf-8', mode='r')  # открытие файла

# Объявление переменных
text = []  # Текст
sentence = []  # Отдельные предложения
direct_speech = False  # прямая речь
ends_of_sentences = ['.', '?', '!']

# Обработка предложений
for line in file:
    for i in range(len(line)):
        symbol = line[i]
        sentence.append(symbol)
        if direct_speech is False:
            if symbol in ends_of_sentences:
                text.append(sentence)
                sentence = []
        if symbol == '"' and direct_speech is False:
            direct_speech = True
        elif symbol == '"' and direct_speech is True:
            direct_speech = False

file.close()

for k in text:
    for j in range(len(k)):
        print(k[j], end="")
    # print(k)
