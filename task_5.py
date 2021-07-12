# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
user_number = int(input('Введите произвольное число: '))

if user_number in my_list:
    my_list.insert(my_list.index(user_number), user_number) # Вставка одинаковых чисел рядом
else:
    if user_number > max(my_list):
        my_list.insert(0, user_number) # Вставка большего числа, отсутствующего в списке
    elif user_number < min (my_list):
        my_list.append(user_number) # Вставка меньшего числа, отсутствующего в списке
    else:
        for item in my_list:
            if user_number < item:
                continue
            else:
                my_list.insert(my_list.index(item), user_number)
                break
print(my_list)