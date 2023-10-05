# Исходный кортеж
languages = ('Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Swift', 'Go')
print("Исходный кортеж: ", languages)

# Создание новых кортежей
new_tu = languages[:3]
print("Первый новый кортеж: ", new_tu)

new_tu2 = languages[3:]
print("Второй новый кортеж: ", new_tu2)

# Объединение всех кортежей
all_tu = new_tu + new_tu2 + languages
print("Объединенный кортеж: ", all_tu)
