                                   # Оператор match
# Оператор match, введенный в Python начиная с версии 3.10, похож на операторы switch-case в других языках программирования. 
# Он позволяет сравнивать значения с несколькими шаблонами и выполнять разные блоки кода в зависимости от того, какой шаблон соответствует значению.
match переменная:
    case шаблон1:
        # виконати код для шаблону 1
    case шаблон2:
        # виконати код для шаблону 2
    case _:
        # виконати код, якщо не знайдено відповідностей

# Оператор match – это своего рода расширенная и более гибкая версия оператора if-elif-else. 
# Он позволяет сравнивать значения с рядом шаблонов и в зависимости от соответствия выполнять определенные действия
fruit = "apple"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")
# В примере fruit – это переменная, значение которой мы хотим проверить:
fruit = "apple"

# Далее оператор match сравнивает значение переменной fruit с каждым значением case последовательно. 
# Если fruit равен "apple", то выполняется блок кода под case "apple":, и на экран выводится "This is an apple."
case "apple":
    print("This is an apple.")

# Если fruit равен "banana", то выведется "This is a banana.", и так далее для "orange". "orange"), то выполняется блок кода под case_:.
case _:
    print("Unknown fruit.")
# Символ _ здесь используется как "заглушка" для указания любых других случаев, которые не соответствуют перечисленным.

# Этот оператор был введен для случаев, когда нам нужно выполнить разные действия в зависимости от значения одной переменной, особенно когда таких вариантов много. 
# Раньше для этого мы использовали длинную цепочку if-elif-else, но теперь оператор match делает код более чистым и более простым для понимания.
# Но оператор имеет более расширенную область использования. Например, использование переменных в шаблонах. 
# Рассмотрим пример:
point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")
# Если значение point=(1,0) то сработает case(x,0): и мы получим вывод Точка лежит на оси X:x=1. 
# Если значение point = (1, 1) сработает уже case (x, y): и будет вывод "Точка имеет координаты: x=1, y=1". 
# В примере используется match для сравнения point с несколькими шаблонами. Если пункт соответствует одному из этих шаблонов, выполняется соответствующий блок кода.

#Также можно использовать оператор match с коллекциями. 
# Например, у нас есть список pets, содержащий названия домашних животных.
pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")
# В этом случае вывод будет "There's a dog.", потому что только "dog" находится на своем месте. 
# Здесь match используется для проверки, содержит ли список pets определенные комбинации животных. 
# Причем важно, что именно комбинации, и именно поэтому у нас сработал case ["dog", _, _]:, а не case ["dog", "cat", _]:, 
# потому что cat в списке pets находится в конце, а не после dog. Знак _ в шаблоне используется как "заполнитель", что означает "любое другое значение".