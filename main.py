from pprint import pprint
import csv
import re

# Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
# Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
# Объединить все дублирующиеся записи о человеке в одну.

# Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

dct = {}
for item in contacts_list[1:]:
    # ФИО
    if len(item[1]) > 0:
        arr = item[1].split(' ')
        if len(arr) > 1:
            item[1], item[2] = arr

    if len(item[0]) > 0:
        arr = item[0].split(' ')
        if len(arr) > 2:
            item[0], item[1], item[2] = arr
        elif len(arr) > 1:
            item[0], item[1] = arr

    # Телефон
    pattern = r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?'
    replace = r'+7(\2)\3-\4-\5\7\8\9'
    item[5] = re.sub(pattern, replace, item[5])
    
    # Дубликаты
    key = f'{item[0]}_{item[1]}'
    if key not in dct:
        dct[key] = item
    else:
        dct[key] = list(map(lambda x: x[0] if len(x[0]) > 0 else x[0] + x[1], zip(dct[key], item)))

contacts_list = contacts_list[:1]
for key in dct:
    contacts_list.append(dct[key])

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    # Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)
