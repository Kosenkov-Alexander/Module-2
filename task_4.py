# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input('Введите текст с пробелами: ')
count = 1
split_string = user_string.split()
for word in split_string:
    if len(word) > 10:
        word = word[:10]
    print(f'{count}.{word}')
    count += 1