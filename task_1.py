'''
Задание №8
Погружение в Python | Коллекции


✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:


✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
'''



friends_items = {'Adam': ('lunch', 'tent', 'marchmellow', 'cole'), 'Jeff': ('lunch', 'tent', 'marchmellow', 'cole'), 
           'Mike': ('knife', 'weapon', 'tent', 'lunch', 'medicine kit')}

# Находим вещи, которые взяли все три друга
common_item = set(friends_items['Adam'])   

for friend, items in friends_items.items():
    common_item = common_item.intersection(set(items))


print(common_item)

# Находим уникальные вещи для каждого друга
unique_items = {}
for friend, items in friends_items.items():
    unique_items[friend] = set(items).difference(common_item)

print(unique_items)


# Находим вещи, которые есть у всех друзей, кроме одного, и имя друга без этой вещи

items_count = {}
for friend, items in friends_items.items():
    for item in items:
        if item in items_count:
            items_count[item] += 1
        else:
            items_count[item] = 1



missing_items = {}
for friend, items in friends_items.items():
    for item in items:
        if items_count[item] == len(friends_items) - 1:
            missing_items[item] = friend

print('Items that everybody has, except of one: ')

for item, friend in missing_items.items():
    print(f'{item} missing from {friend}')







