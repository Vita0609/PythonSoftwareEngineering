'''
   Методы списков
Списки в Python — это изменяемые последовательности, которые могут содержать элементы разных типов. Вот некоторые основные методы списков:

1. append()
Добавляет элемент в конец списка.
my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]

2. extend()
Добавляет элементы из другого списка.
my_list.extend([5, 6])  # [1, 2, 3, 4, 5, 6]

3. insert()
Вставляет элемент по указанному индексу.
my_list.insert(1, 'a')  # [1, 'a', 2, 3, 4, 5, 6]

4. remove()
Удаляет первый элемент с указанным значением.
my_list.remove(3)  # [1, 'a', 2, 4, 5, 6]

5. pop()
Удаляет элемент по указанному индексу и возвращает его. Если индекс не указан, удаляет последний элемент.
last_element = my_list.pop()  # last_element = 6, my_list = [1, 'a', 2, 4, 5]

6. sort()
Сортирует элементы списка на месте.
my_list.sort()  # Сортирует список по возрастанию

7. reverse()
Разворачивает элементы списка на месте.
my_list.reverse()  # Разворачивает список

8. count()
Возвращает количество вхождений указанного элемента.
count_a = my_list.count('a')  # Возвращает количество 'a' в списке

9. index()
Возвращает индекс первого вхождения указанного элемента.
index_a = my_list.index('a')  # Возвращает индекс 'a'

***Методы строк
Строки в Python — это неизменяемые последовательности символов. Вот некоторые основные методы строк:

1. upper()
Возвращает строку в верхнем регистре.
my_string = "hello"
upper_string = my_string.upper()  # "HELLO"

2. lower()
Возвращает строку в нижнем регистре.
lower_string = my_string.lower()  # "hello"

3. strip()
Удаляет пробелы в начале и конце строки.
my_string = "  hello  "
stripped_string = my_string.strip()  # "hello"

4. replace()
Заменяет подстроку на другую.
new_string = my_string.replace("l", "p")  # "heppo"

5. split()
Разделяет строку на части по указанному разделителю и возвращает список.
my_string = "hello world"
split_string = my_string.split()  # ['hello', 'world']

6. join()
Объединяет элементы списка в строку с указанным разделителем.
my_list = ['hello', 'world']
joined_string = ' '.join(my_list)  # "hello world"

7. find()
Возвращает индекс первого вхождения подстроки, или -1, если не найдено.
index = my_string.find("l")  # Возвращает индекс первого 'l'

8. startswith() и endswith()
Проверяют, начинается или заканчивается ли строка на указанную подстроку.
my_string.startswith("he")  # True
my_string.endswith("lo")     # False

9. format()
Форматирует строку, вставляя значения в указанные места.
formatted_string = "Hello, {}".format("world")  # "Hello, world"

***Заключение
Списки и строки в Python имеют множество полезных методов, которые упрощают работу с данными. Если у вас есть дополнительные вопросы или вам нужно больше примеров, дайте знать!

                  **методы строк
capitalize()
Преобразует первый символ строки в верхний регистр.
my_string = "hello"
print(my_string.capitalize())  # "Hello"
casefold()

Преобразует строку в нижний регистр, более агрессивный, чем lower(), для сравнения.
my_string = "HELLO"
print(my_string.casefold())  # "hello"
center(width, fillchar)

Выравнивает строку по центру в заданной ширине, заполняя пустое пространство указанным символом.
my_string = "hello"
print(my_string.center(10, '*'))  # "***hello***"
count(substring)

Возвращает количество неперекрывающихся вхождений подстроки.
my_string = "hello world"
print(my_string.count("o"))  # 2
endswith(suffix)

Проверяет, заканчивается ли строка на указанную подстроку.
my_string = "hello world"
print(my_string.endswith("world"))  # True
find(substring)

Возвращает индекс первого вхождения подстроки или -1, если подстрока не найдена.
my_string = "hello world"
print(my_string.find("o"))  # 4
format(*args, **kwargs)

Форматирует строку, вставляя значения в указанные места.
name = "Alice"
greeting = "Hello, {}".format(name)  # "Hello, Alice"
index(substring)

Возвращает индекс первого вхождения подстроки. Вызывает ошибку, если подстрока не найдена.
my_string = "hello world"
print(my_string.index("o"))  # 4
isalnum()

Проверяет, состоит ли строка только из алфавитных символов и цифр.
my_string = "hello123"
print(my_string.isalnum())  # True
isalpha()

Проверяет, состоит ли строка только из алфавитных символов.
my_string = "hello"
print(my_string.isalpha())  # True
isdigit()

Проверяет, состоит ли строка только из цифр.
my_string = "12345"
print(my_string.isdigit())  # True
isspace()

Проверяет, состоит ли строка только из пробелов.
my_string = "   "
print(my_string.isspace())  # True
join(iterable)

Объединяет элементы из итерируемого объекта в строку с указанным разделителем.
my_list = ['Hello', 'world']
print(' '.join(my_list))  # "Hello world"
lower()

Преобразует все символы строки в нижний регистр.
my_string = "HELLO"
print(my_string.lower())  # "hello"
lstrip(chars)

Удаляет указанные символы (по умолчанию пробелы) слева от строки.
my_string = "   hello"
print(my_string.lstrip())  # "hello"
rstrip(chars)

Удаляет указанные символы (по умолчанию пробелы) справа от строки.
my_string = "hello   "
print(my_string.rstrip())  # "hello"
strip(chars)

Удаляет указанные символы (по умолчанию пробелы) с обеих сторон строки.
my_string = "   hello   "
print(my_string.strip())  # "hello"
replace(old, new)

Заменяет все вхождения подстроки old на new.
my_string = "hello world"
print(my_string.replace("world", "Python"))  # "hello Python"
split(separator)

Разделяет строку по указанному разделителю и возвращает список подстрок.
my_string = "hello world"
print(my_string.split())  # ['hello', 'world']
startswith(prefix)

Проверяет, начинается ли строка с указанной подстроки.
my_string = "hello world"
print(my_string.startswith("hello"))  # True
title()

Преобразует строку в формат "титула", где каждое слово начинается с заглавной буквы.
my_string = "hello world"
print(my_string.title())  # "Hello World"
upper()

Преобразует все символы строки в верхний регистр.
my_string = "hello"
print(my_string.upper())  # "HELLO"'''