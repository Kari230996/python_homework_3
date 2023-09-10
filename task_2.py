'''
2. Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
'''

list_ = [1, 1, 2, 'cat', 'lion', 3, 2, 'donkey', 'lion', True, False, False]

dublicates = []
result = []

for i in list_:
    if i not in result:
        result.append(i)
    elif i not in dublicates:
        dublicates.append(i)
   
print(dublicates)