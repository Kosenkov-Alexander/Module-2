# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

i = 0
some_list = []
for item in range(0, 7):
    item = int(input('Введите значение: '))
    some_list.append(item)

count = len(some_list) // 2
while i <= count:
    some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
    i += 2
print(some_list)