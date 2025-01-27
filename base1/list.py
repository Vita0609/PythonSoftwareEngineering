# В Python списки (list) — это изменяемые, упорядоченные коллекции, которые могут содержать элементы разных типов данных, включая другие коллекции. 
# Списки часто используются для хранения и обработки данных.

# Создание списка:
lst = [1, 2, 3]
empty_list = []  # Пустой список

# Доступ к элементам списка:
lst = [10, 20, 30]
print(lst[0])  # 10
print(lst[-1])  # 30 (обращение с конца)

# Изменение элементов списка:
lst[1] = 25
print(lst)  # [10, 25, 30]

                    # Добавление элементов: 
# Метод append() добавляет элемент в конец списка:
lst.append(40)
print(lst)  # [10, 25, 30, 40]

# Метод insert() вставляет элемент на заданную позицию
lst.insert(1, 15)  # Вставляем 15 на позицию с индексом 1
print(lst)  # [10, 15, 25, 30, 40]

                    # Удаление элементов:
# Метод remove() удаляет первый найденный элемент:
lst.remove(25)
print(lst)  # [10, 15, 30, 40]

# Метод pop() удаляет элемент по индексу (по умолчанию удаляет последний):
lst.pop()  # Удаляет последний элемент
print(lst)  # [10, 15, 30]

# Итерация по списку:
for item in lst:
    print(item)

                      # Методы для работы с элементами:
# index() — находит индекс первого вхождения элемента:
print(lst.index(15))  # 1

# count() — считает количество вхождений элемента:
print(lst.count(10))  # 1

      # Метод sort() для сортировки списка:
lst = [30, 10, 40, 20]
lst.sort()  # По возрастанию
print(lst)  # [10, 20, 30, 40]

       # Метод reverse() для разворота списка:
lst.reverse()
print(lst)  # [40, 30, 20, 10]

        # Метод clear() для очистки списка:
lst.clear()
print(lst)  # []

                        # Генерация списков
# Списковые выражения (list comprehensions) позволяют создавать новые списки на основе существующих:
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

                         # Другие полезные функции и методы:
# len() — возвращает количество элементов в списке:
print(len(lst))  # 4

# sum() — находит сумму всех числовых элементов списка:
print(sum(lst))  # 100 (если lst = [10, 20, 30, 40])

# max() и min() — находят максимальное и минимальное значение:
print(max(lst))  # 40
print(min(lst))  # 10

# Списки в Python — это мощный инструмент для работы с коллекциями данных, и методы, описанные выше, позволяют легко и эффективно манипулировать данными в списках.
                     



