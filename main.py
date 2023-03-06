from pprint import pprint
import csv
import re

# Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# 1. Выполните пункты 1-3 задания.
# Ваш код

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    # Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)
