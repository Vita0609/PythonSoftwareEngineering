# В Python для повторяющихся операций используются циклы.
#  Два основных типа циклов — это for и while. Оба цикла позволяют выполнять один и тот же блок кода несколько раз, но с разными условиями и механизмами работы.

                                         # Цикл for
# Цикл for используется для перебора элементов в последовательности (например, списка, строки, диапазона чисел) и выполнения блока кода для каждого элемента.
# Синтаксис:
for item in iterable:
    # действия с item

# Пример:
for i in range(5):  # перебираем числа от 0 до 4
    print(i)

                                        # Методы и функции для for:
# range(start, stop, step): Генерирует последовательность чисел от start до stop с шагом step. 
# Это полезно для перебора числовых диапазонов.
for i in range(1, 10, 2):  # от 1 до 9 с шагом 2
    print(i)

# enumerate(): Возвращает пару (индекс, значение) для каждого элемента в итерируемом объекте.
lst = ['a', 'b', 'c']
for index, value in enumerate(lst):
    print(f'Индекс: {index}, Значение: {value}')

# zip(): Объединяет несколько итерируемых объектов в один.
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 30, 22]
for name, age in zip(names, ages):
    print(f'{name} - {age} лет')

                                            # Цикл while
# Цикл while выполняет блок кода до тех пор, пока заданное условие истинно. 
# Этот цикл часто используется, когда неизвестно заранее, сколько раз нужно выполнить блок кода.

# Синтаксис:
while condition:
    # действия

# Пример:
count = 0
while count < 5:
    print(count)
    count += 1

                                            # Методы и функции для while:
# break: Прерывает выполнение цикла, даже если условие еще истинно.
for i in range(10):
    if i == 5:
        break  # Прерывает цикл, когда i равно 5
    print(i)

# continue: Пропускает текущую итерацию цикла и переходит к следующей.
for i in range(5):
    if i == 3:
        continue  # Пропускает вывод числа 3
    print(i)

# else с циклами: После завершения цикла (если он не был прерван с помощью break), выполняется блок else.
for i in range(5):
    print(i)
else:
    print("Цикл завершен.")

# Пример использования циклов:
# Циклы могут быть полезны в различных ситуациях. Например, чтобы найти сумму чисел от 1 до 10:
sum_numbers = 0
for i in range(1, 11):
    sum_numbers += i
print(sum_numbers)  # Выводит 55

# Циклы в Python — это мощный инструмент для выполнения повторяющихся операций. 
# Важно выбрать подходящий тип цикла в зависимости от задачи. 
# Цикл for идеально подходит для перебора элементов, тогда как while хорош для случаев, когда нужно выполнить код, пока выполняется условие.

# Цикл for Python используется для итерации по элементам любой последовательности (например, списка, кортежа, строки) или других итерированных объектов;
for element in sequence:
    # виконувати дії з element

# Цикл while выполняет блок кода, пока заданное условие истинно (True). Как только условие становится ложным (False), цикл заканчивается
while condition:
    # виконувати дії, поки condition є True

                              # Цикл FOR
# В Python цикл for используется для выбора всех элементов контейнеров или итерированных объектов, например списков. Инструкции, находящиеся в теле цикла, будут исполнены столько раз, сколько элементов в коллекции.
# При этом на каждой итерации специальная переменная приобретает значение одного из элементов коллекции.
# Работу цикла for сравнима с тем, что вы по очереди возьмете каждую букву из фразы и произнесете ее. 
# Фразой может выступать строка 'apple', а аналогом произнесения вслух будет выступать вывод соответствующей буквы в консоль.  
fruit = 'apple'
for char in fruit:
    print(char)

# Синтаксис цикла for в Python включает в себя несколько важных компонентов:

# Цикл начинается с ключевого слова for, указывающего на начало цикла.
# После for следует название переменной, которая будет использоваться для хранения текущего значения итерации. 
# Значение этого переменного будет изменяться с каждой итерацией цикла.
# Далее следует ключевое слово in, указывающее на объект или диапазон, по которому будет происходить итерация.
# После in размещается объект или выражение, определяющее набор элементов или диапазон, по которому будет происходить итерация.
# В конце строки ставится двоеточие:, отделяющее заглавие цикла от его тела.
# На новой строке с отступлением от начала строки размещаются инструкции или выражения, которые следует выполнять на каждой итерации. 
# Отступление является обязательным, поскольку он определяет блок кода, относящийся к циклу.         
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")
# У прикладі літери алфавіту з alphabet виводяться в консоль по черзі, через пробіл.
#  a b c d e f g h i j k l m n o p q r s t u v w x y z

# Використаємо цикл for у Python для ітерації по елементах ітерованого об'єкта, у нашому випадку — списку some_iterable.

some_iterable = ["a", "b", "c"]

for i in some_iterable:
    print(i)
# Цикл for используется для последовательного прохождения по каждому элементу списка some_iterable. В этом цикле i является переменной, которая на каждой итерации принимает значение текущего элемента some_iterable. На каждой итерации выполняется команда print(i), выводящая текущий элемент списка.
# Цикл for может использоваться для выбора всех чисел в списке и получения результата для каждого числа: 
odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)
                                           