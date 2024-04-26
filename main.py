import os,json
from get_block.get_block_by_index_linear import get_block_by_index_linear
from get_block.get_block_by_index_binary import get_block_by_index_binary
from sort.bubble_sort import bubble_sort
from sort.selection_sort import selection_sort
from datetime import datetime,date

files = []
l = []
files += os.listdir('transactions')
for i in files:
    f = open(f"{'transactions'}/{i}")
    l.append(json.loads(f.read()))
a = l.copy()

first = a[0]  # Искомый элемент находится в начале
end = a[-1]  # Искомый элемент находится в конце
mid = a[len(a)//2]  # Искомый элемент находится в центре
dvad = a[len(a)-20]  # Искомый элемент находится на 20 месте с конца

temp = [first, end, mid, dvad]

# Задание1
z_1 = True
if z_1:
    print("Линейный поиск:")
    for i in temp:
        print(f"Линейный поиск индекса №{i['index']}: ", get_block_by_index_linear(a, i['index']), sep="\n", end="\n")



    print("Линейный поиск:")# отсортированый массив
    for i in temp:
        print(f"Линейный поиск индекса №{i['index']}: ", get_block_by_index_linear(sorted(a, key=lambda x: x['index']), i['index']), sep="\n", end="\n")

   

    print("Бинарный поиск:")
    for i in temp:
        print(f"Бинарный поиск индекса №{i['index']}: ", get_block_by_index_binary(a, i['index']), sep="\n", end="\n")
#Задание 2
z_2 = True

if z_2:
    print(f"Неотсортированый массив:\n")
    print(f"Сортировка пузьрьком:\n{bubble_sort(a)}")
    print(f"Сортировка выбором:\n{selection_sort(a)}")
#Задание 3
z_3 = True
if z_3:
    count_of_transactions = 0
    ct = 0
    third = sorted(a, key=lambda x: x['index'])
    miners = dict()

    for i in third:
        count_of_transactions += len(i['transactions'])
        ct += len(list(filter(lambda x: x['from'] != "SYSTEM" and i['index'] != 0, i['transactions'])))
        print(f"Номер блока: {i['index']}. Количество транзакций : {len(i['transactions'])}")
    print(f"Общее количество транзакций: {count_of_transactions} ; {ct} (без учёта SYSTEM)\n")

    list_of_values = []
    list_of_transactions = []

    for i in third: # Суммарное количество вознаграждений
        if i["index"] == 0:
            continue
        list_of_values.append(i["transactions"][-1]["value"])
        if i['transactions'][-1]['to'] not in miners:
            miners[i['transactions'][-1]['to']] = 0 # Добавление майнера в словарь
        miners[i['transactions'][-1]['to']] += i['transactions'][-1]['value'] # Добавление награжденй
    miners = sorted(miners.items(), key=lambda x: x[1])
    list_of_values = sorted(list_of_values)

    print(f"Самое низкое  вознаграждение : {miners[0]}\nСамое высокое  вознаграждение : {miners[-1]}\n")
    print(f"Самое низкое вознаграждение : {list_of_values[0]}\nСамое высокое вознаграждение : {list_of_values[-1]}\n")

    for i in third:
        if i["index"] == 0:
            continue
        for j in i["transactions"]:
            if j['from'] == "SYSTEM":
                continue
            list_of_transactions.append(j["value"])
    print(f"Среднее значение перевода в транзакциях : {sum(list_of_transactions)/len(list_of_transactions)}")

    minutes = dict()

    for i in third:
        minute = datetime.fromtimestamp(i['timestamp']).minute
        if minute not in minutes:
            minutes[minute] = 0
        else:
            minutes[minute] += 1

    print("\n Минуты:")
    for key, val in minutes.items():
        print(f"{key} м.: {val}")
    
