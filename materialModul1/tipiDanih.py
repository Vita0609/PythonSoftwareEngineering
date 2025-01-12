'''
1. Примитивные (основные) типы данных
***Числовые типы***

***int — целые числа:
x = 10
y = -5

***float — числа с плавающей точкой:
pi = 3.14
e = -2.718

complex — комплексные числа:
z = 3 + 4j

        ***Логический тип***

bool — логические значения:
is_active = True
is_closed = False

Текстовый тип
str — строки (последовательность символов):
name = "Alice"
greeting = 'Hello, World!'

2. Коллекции (структурированные типы данных)

*Списки
list — упорядоченные изменяемые коллекции:
numbers = [1, 2, 3, 4]
fruits = ["apple", "banana", "cherry"]

*Кортежи
tuple — упорядоченные неизменяемые коллекции:
coordinates = (10, 20)

*Множества
set — неупорядоченные уникальные элементы:
unique_numbers = {1, 2, 3, 3}  # {1, 2, 3}
frozenset — неизменяемое множество:
frozen_set = frozenset({1, 2, 3})

*Словари
dict — коллекции пар "ключ-значение":
person = {"name": "Alice", "age": 25}


3. Специальные типы данных
NoneType
None — специальное значение, которое обозначает "ничто":
result = None

Диапазоны
range — последовательность чисел:
numbers = range(5)  # [0, 1, 2, 3, 4]

Байтовые типы
bytes — последовательность байтов (неизменяемая):
b = b"hello"
bytearray — изменяемая последовательность байтов:
ba = bytearray(b"hello")
ba[0] = 97
memoryview — обертка над байтовыми объектами:
mv = memoryview(b"hello")

4. Пользовательские типы
Вы можете создавать свои собственные типы данных, используя классы:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)

5. Операции над типами
Узнать тип объекта:
print(type(10))         # <class 'int'>
print(type("Hello"))    # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>

Проверить тип:
x = 10
if isinstance(x, int):
    print("x — это целое число")

Таблица основных типов
Тип	Пример	Изменяемый?
int	10, -5	Нет
float	3.14, -2.71	Нет
complex	3 + 4j	Нет
bool	True, False	Нет
str	"hello"	Нет
list	[1, 2, 3]	Да
tuple	(1, 2, 3)	Нет
set	{1, 2, 3}	Да
frozenset	frozenset({1, 2, 3})	Нет
dict	{"key": "value"}	Да
bytes	b"hello"	Нет
bytearray	bytearray(b"hello")	Да
NoneType	None	-
'''