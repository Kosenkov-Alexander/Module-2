# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_number = input('Введите номер месяца от 1 до 12: ')
weather = ['Лето', 'Осень', 'Зима', 'Весна']

months = {
    '1': weather[2],
    '2': weather[2],
    '3': weather[3],
    '4': weather[3],
    '5': weather[3],
    '6': weather[0],
    '7': weather[0],
    '8': weather[0],
    '9': weather[1],
    '10': weather[1],
    '11': weather[1],
    '12': weather[2]
}
print(months[user_number])