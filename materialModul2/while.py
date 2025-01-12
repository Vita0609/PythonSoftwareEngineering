'''
Цикл while в Python выполняет блок кода до тех пор, пока заданное условие истинно (True). 
Это позволяет создавать повторяющиеся задачи с неизвестным заранее количеством итераций.

while условие:
    # Код, который выполняется, пока условие True
    ...

Пример 1: Простой цикл
Вывод чисел от 1 до 5:

i = 1
while i <= 5:
    print(i)
    i += 1
Результат:
1
2
3
4
5

Пример 2: Использование break
Цикл можно прервать с помощью команды break:
i = 1
while True:  # Бесконечный цикл
    print(i)
    if i == 3:  # Условие выхода
        break
    i += 1
Результат:
1
2
3

Пример 3: Использование continue
Пропуск текущей итерации:
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Пропускаем число 3
    print(i)
Результат:
1
2
4
5


Пример 4: Цикл с пользовательским вводом
Считать ввод, пока пользователь не введёт "стоп":
while True:
    user_input = input("Введите команду (или 'стоп' для выхода): ")
    if user_input.lower() == "стоп":
        print("Программа завершена.")
        break
    print(f"Вы ввели: {user_input}")

Пример 5: Цикл с дополнительным условием else
Блок else выполняется, если цикл завершился естественным образом (без break):
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Цикл завершён.")
Результат:
1
2
3
Цикл завершён.

Потенциальные ошибки:
Бесконечный цикл: Если не изменить переменную в условии, цикл будет работать бесконечно:
i = 1
while i <= 5:  # Условие всегда True
    print(i)

Ошибка с типом данных: При сравнении типов данных нужно быть внимательным:
x = "5"
while x < 10:  # Ошибка, так как строка не сравнима с числом
    print(x)

'''
# пример 
# Этот код реализует бесконечный цикл, в котором пользователь вводит команды. Цикл будет продолжаться до тех пор, пока пользователь не введёт "exit". Вот как он работает:
while True:
    user_input = input("Введите команду ( '>>>' ): ")  # Просим ввести команду
    if user_input == "exit":  # Проверяем, ввёл ли пользователь "exit"
        break  # Если ввёл, выходим из цикла
    print(f"You write: {user_input}")  # Иначе выводим сообщение с введённым текстом

'''
Объяснение:
while True: Создаёт бесконечный цикл.
input: Ждёт пользовательского ввода.
if user_input == "exit": Если пользователь ввёл слово "exit", программа выходит из цикла.
print(f"You write: {user_input}"): Показывает, что ввёл пользователь.'''