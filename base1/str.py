# Строки в Python — это последовательности символов, которые можно изменять с помощью различных методов. 
# Вот некоторые важнейшие методы работы со строками:

                  # Основные методы строк:
# .upper() — преобразует все символы строки в верхний регистр:
text = "hello"
print(text.upper())  # "HELLO"

# .lower() — преобразует все символы строки в нижний регистр:
text = "HELLO"
print(text.lower())  # "hello"

# .strip() — удаляет пробелы в начале и конце строки:
text = "  hello  "
print(text.strip())  # "hello"

# .replace(old, new) — заменяет все вхождения подстроки old на подстроку new:
text = "hello world"
print(text.replace("world", "Python"))  # "hello Python"

# .split(separator) — разбивает строку на части по разделителю:
text = "apple,banana,cherry"
print(text.split(","))  # ['apple', 'banana', 'cherry']

# .find(substring) — находит индекс первого вхождения подстроки в строку. Возвращает -1, если подстрока не найдена:
text = "hello"
print(text.find("e"))  # 1
print(text.find("z"))  # -1

# 