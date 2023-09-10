'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
'''

items = {
    "палатка": 2,
    "спальник": 1,
    "еда": 3,
    "вода": 2,
    "фонарик": 0.5,
    "лекарства": 1.5
}

# Максимальная грузоподъемность рюкзака
max_capacity = 5

# Создаем список для вещей, которые будут помещены в рюкзак
selected_items = []

# Сортируем вещи по массе в убывающем порядке
sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)

# Заполняем рюкзак

current_capacity = 0

for item, weight in sorted_items:
    if current_capacity + weight <= max_capacity:
        selected_items.append(item)

        current_capacity += weight

print("Вещи, которые поместились в рюкзак:")
for item in selected_items:
    print(item)
    

