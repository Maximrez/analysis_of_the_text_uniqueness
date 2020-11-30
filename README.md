# Название: AnalysisTextUniqueness
#### Задача: Разработка программы проверки текста на заимствования.

Расстояние Жаккарда, используемое для нахождения сходств в текстах, подразумевает двустороннее вхождение.
Заимствованность предложения в программе определяется как частное числа элементов пересечения множеств мешков слов
исходного предложения и текста найденной страницы и количества уникальных слов в исходном предложении. 

##### Описание работы программы:
1. Запуск программы с подачей названия файла в качестве аргумента или в стандартном вводе
2. Открытие файла и чтение (пока доступен только формат .txt), обработка возможных ошибок (неправильное название,
отсутствие файла)
3. Обработка текста, разделение на предложения, разделение на слова
4. Поиск предложений, число уникальных слов в которых больше 7, в google через rapiapi
5. Определение заимствованности предложения в найденных страницах с помощью описанного ранее алгоритма
6. Вывод результатов работы программы: наиболее заимствованных предложений, наиболее используемых ссылок,
всех предложений с указанием их заимствованности и ссылки на ресурс
7. Запись результатов работы программы в файл с названием result_ + название исходного файла в директорию расположения
исходного файла

Выявлена следующая метрика работы программы:
60% и менее- низкая заимствованность;
от 60 до 90% - средняя заимствованность;
90% и более - высокая заимствованность.

В директории data есть файл с текстом referat_history.txt и результат работы программы на этом файле
result_referat_history.txt
