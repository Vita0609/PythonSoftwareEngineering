# Рекурсия — это процесс, при котором функция вызывает сама себя. 
# Это мощный инструмент в программировании, особенно для решения задач, которые могут быть разбиты на более простые подзадачи. 
# Рекурсия используется в различных задачах, например, при поиске в деревьях, обработке графов, решении математических задач 
# (например, вычисление факториала или чисел Фибоначчи).

                              # Основные элементы рекурсии:
#  Базовый случай (Base case) — это условие, при котором функция больше не вызывает себя, чтобы избежать бесконечного цикла.
#  Рекурсивный случай — это вызов функции самой себя с новыми параметрами.
# Пример рекурсии на Python:
# Пример вычисления факториала с использованием рекурсии

def factorial(n):
    if n == 0:  # Базовый случай
        return 1
    else:  # Рекурсивный случай
        return n * factorial(n - 1)

print(factorial(5))  # Вывод: 120

# Базовый случай: когда n == 0, факториал равен 1.
# Рекурсивный случай: функция вызывает сама себя, передавая уменьшенное значение n.

                                     # Преимущества и недостатки рекурсии:
        # Преимущества:
# Простота решения некоторых задач (например, обход деревьев и графов).
# Рекурсия может сделать код более элегантным и понятным.
        # Недостатки:
# Рекурсия может быть неэффективной, особенно если не реализован правильный базовый случай или если функция выполняет много лишних вызовов.
# Может привести к переполнению стека, если рекурсивные вызовы слишком глубоки (например, в случае слишком большого количества рекурсивных вызовов).

                                       # Рекурсия и итерация:
# Некоторые задачи, которые могут быть решены с помощью рекурсии, также могут быть решены с использованием цикла (итерации). 
# В таких случаях рекурсия может быть менее эффективной из-за затрат на память и время. 
# В Python существуют ограничения по глубине рекурсии (по умолчанию 1000 рекурсивных вызовов), но это можно изменить 
# с помощью sys.setrecursionlimit(), если необходимо.  
# Итеративный способ вычисления факториала

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # Вывод: 120

              # Рекурсия часто используется для решения таких задач, как:

# Обход деревьев (например, файловая система).
# Алгоритмы сортировки, такие как быстрая сортировка и сортировка слиянием.
# Решение задач, которые можно разбить на подзадачи (например, нахождение всех подстрок строки).
# Рекурсия является важным концептом, который нужно понимать и правильно использовать для эффективного решения проблем в программировании.
      
                                     # Стек
# Стек вызовов – это специфическая часть памяти, которая используется для хранения информации об активных вызовах функций.
#  Каждый раз, когда функция вызывается, создается новая запись (или "слой") в этом стеке для этого конкретного вызова. 
# Этот слой содержит информацию о переменных функциях, ее параметрах и месте, откуда была вызвана функция, чтобы по завершении выполнения функции программа могла продолжить работу с правильного места.
# Так что когда функция вызывает себя рекурсивно, каждый новый вызов функции сохраняется в стеке вызовов. 
# Сам стек вызовов создает интерпретатор Python при выполнении программы.
# Если представить стек как стопку книг, где каждая новая книга, которую вы кладете сверху, отображает новый вызов функции, то рекурсия – это добавление новых книг вверх стопки. 
# Когда функция завершает свою работу, "книга" снимается со стопки, и мы "возвращаемся" к предыдущей книге.
# Итак, когда базовый случай достигнут, вызовы функций начинают разгружаться со стека, что позволяет рассчитать конечный результат.
# Рассмотрим пример кода, показывающего, как работает стек вызовов в рекурсии на примере функции для вычисления факториала числа:
def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))
# Этот код вычисляет факториал числа 5, равный 5*4*3*2*1=120. 
# Когда вы запустите этот код, вы увидите последовательность вызовов рекурсивной функции и возвращения результатов.
# Этот пример показывает, как каждый вызов рекурсивной функции добавляет новый "слой" в стек вызовов, а каждый возвращенный результат удаляет "слой".
# Произведем углубленный анализ нашего примера с факториалом и добавим иллюстрации.
# Когда вы вызываете factorial(5), создается первый слой в стеке вызовов для этого вызова. будет достигнут базовый случай factorial(1). 
# В этот момент рекурсия достигла своей наибольшей глубины, и стек вызовов содержит пять слоев.
# Завершение выполнения factorial(1) начинает процесс "разгрузки" стека.
# Каждый слой, начиная с последнего, обрабатывается, и результат каждого вызова возвращается к предыдущему вызову до тех пор, 
# пока весь стек не будет обработан, и мы не получим конечный результат для factorial(5).

# Рекурсивные функции удобны в ситуациях, когда мы заранее не знаем, сколько раз нужно будет вызывать функцию, например, при разборе директорий на диске. 
# Приложение не знает заранее, насколько глубока структура директорий и каков у них уровень вложенности.
#  И чтобы перебрать все файлы во всех вложенных директориях, функция должна вызвать сама себя, встречая очередную директорию. 
# Такая функция, которая вызывает сама себя в некоторых условиях, называется рекурсивной.