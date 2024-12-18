# Множество в Python — это неупорядоченная коллекция уникальных элементов.
#  Множества полезны, когда нужно хранить уникальные значения и выполнять операции, такие как объединение, пересечение и разность, над множествами.

                                   # Создание множества
# Множества создаются с помощью фигурных скобок {} или с использованием встроенной функции set().
# Пример создания множества
my_set = {1, 2, 3, 4}
print(my_set)  # {1, 2, 3, 4}

# Использование функции set()
another_set = set([1, 2, 3, 4])
print(another_set)  # {1, 2, 3, 4}

                                      # Особенности множеств:
# !.Уникальность элементов: Множество не может содержать дубликатов.
# 2.Неупорядоченность: Элементы множества не имеют индексов, и порядок их хранения не гарантируется.
# 3.Изменяемость: Множество можно изменять, добавлять и удалять элементы.

                                      # Операции с множествами
# Python поддерживает различные операции для работы с множествами, такие как объединение, пересечение, разность и симметричная разность.

                                      # Добавление элементов
# Можно добавлять элементы в множество с помощью метода .add().
my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}

                                      # Удаление элементов
# Для удаления элементов можно использовать метод .remove() или .discard(). 
# Метод .remove() вызывает ошибку, если элемента нет в множестве, в то время как 
# .discard() безопасен (не вызывает ошибку).
my_set.remove(4)  # Удаляет 4
# my_set.remove(10)  # Ошибка, если элемента нет

my_set.discard(5)  # Удаляет 5, но не вызывает ошибку, если элемента нет

                                     # Очистка множества
# Чтобы очистить множество, используйте метод .clear().
my_set.clear()
print(my_set)  # set()

                           # Основные методы множества
# .add(element) — добавляет элемент в множество.
# .remove(element) — удаляет элемент (если элемент отсутствует, вызывает ошибку).
# .discard(element) — удаляет элемент (если элемента нет, не вызывает ошибку).
# .pop() — удаляет и возвращает произвольный элемент множества.
# .clear() — очищает множество.
# .union(other_set) — объединяет два множества.
# .intersection(other_set) — находит пересечение двух множеств.
# .difference(other_set) — находит разницу между двумя множествами.
# .symmetric_difference(other_set) — находит симметричную разность.

                           # Операции с множествами
# Объединение: возвращает новое множество, содержащее все элементы обоих множеств.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # или set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5}

# Пересечение: возвращает новое множество, содержащее только те элементы, которые есть в обоих множествах.
intersection_set = set1 & set2  # или set1.intersection(set2)
print(intersection_set)  # {3}

# Разность: возвращает множество элементов, которые есть в одном множестве, но нет в другом.
difference_set = set1 - set2  # или set1.difference(set2)
print(difference_set)  # {1, 2}

# Симметричная разность: возвращает множество элементов, которые есть в одном из множеств, но не в обоих.
symmetric_difference_set = set1 ^ set2  # или set1.symmetric_difference(set2)
print(symmetric_difference_set)  # {1, 2, 4, 5}

# Перебор множества
# Для перебора элементов множества используется цикл for, но нужно помнить, что порядок элементов в множестве не гарантируется. 
for elem in my_set:
    print(elem)

# Создание множества
my_set = {1, 2, 3, 4, 5}

# Добавление элемента
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# Удаление элемента
my_set.remove(4)
print(my_set)  # {1, 2, 3, 5, 6}

# Пересечение множеств
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  # {3}

# Объединение множеств
print(set1 | set2)  # {1, 2, 3, 4, 5}

# Разность множеств
print(set1 - set2)  # {1, 2}

# Преимущества множества:
# Отсутствие дубликатов: множество автоматически удаляет повторяющиеся элементы.
# Быстрые операции: операции с множествами, такие как проверка на наличие элемента, добавление и удаление, выполняются очень быстро.
# Поддержка математических операций: множества поддерживают все стандартные математические операции, такие как объединение, пересечение и разность.