def search_normalize(searches):
    searches1 = []
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    replaceable = ['...', '\xa0', '- ', '(', ')', ',', ';', '́', '«', '»', '.', '"', ':', '”', '“', '—', '-', "'"]
    for i in range(len(searches)):
        if len(searches[i]["sentence"].split()) < 5:
            continue
        search = dict()
        search["sentence"] = searches[i]["sentence"]
        search["results"] = list()
        for result in searches[i]["results"]:
            if result["description"] != '':
                res = dict()
                res["description"] = (result["description"].rstrip()).lower()
                res["link"] = result["link"]

                if (res["description"].split())[0] in months:
                    res["description"] = ' '.join((res["description"].split())[4:])
                elif res["description"][4] == res["description"][7] == '/':
                    res["description"] = ' '.join((res["description"].split())[2:])
                elif res["description"].split()[0][-1] == res["description"].split()[1][-1] == \
                        res["description"].split()[2][-1] == '.' and res["description"].split()[3] == '—':
                    res["description"] = ' '.join((res["description"].split())[4:])
                elif res["description"][2] == res["description"][5] == '.':
                    res["description"] = ' '.join((res["description"].split())[2:])
                elif res["description"].split()[0] in list(map(str, range(1, 32))) and res["description"].split()[
                    2] in list(map(str, range(1900, 2100))):
                    res["description"] = ' '.join((res["description"].split())[4:])
                elif res["description"].split()[0] in list(map(str, range(1, 32))) and res["description"].split()[
                    4] in list(map(str, range(1900, 2100))):
                    res["description"] = ' '.join((res["description"].split())[6:])
                for r in replaceable:
                    res["description"] = res["description"].replace(r, '')

                search["results"].append(res)
        if len(search["results"]) != 0:
            searches1.append(search)
    return searches1


def non_uniqueness(searches, file_name):
    avrg = 0
    avrg_c = 0

    f = open(file_name, "w", encoding="utf-8")

    for search in searches:
        maximum = 0
        maximum_link = ''

        sntnc = search["sentence"].lower()

        replaceable = ['...', '\xa0', '- ', '(', ')', ',', ';', '́', '«', '»', '.', '"', ':', '”', '“', '—', '-', "'"]
        for r in replaceable:
            sntnc = sntnc.replace(r, '')
        sntnc = sntnc.split()

        uniq_words_s = set(sntnc)
        for result in search["results"]:
            uniq_words_r = set(result["description"].split())
            non_uniqueness = len(uniq_words_s.intersection(uniq_words_r)) / len(uniq_words_s)
            if non_uniqueness > maximum:
                maximum = non_uniqueness
                maximum_link = result['link']
            if maximum == 1:
                break

        avrg += maximum
        avrg_c += 1

        f.write(search["sentence"] + "\n")
        f.write(str(round(maximum, 2)) + "\n")
        f.write(maximum_link + "\n")
        f.write("\n")

    f.write(str(round(avrg * 100 / avrg_c, 1)) + "%")
    f.close()
