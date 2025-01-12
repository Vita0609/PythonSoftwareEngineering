'''
Методы словарей в Python

clear()
Удаляет все элементы из словаря.
my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)  # {}

copy()
Возвращает поверхностную копию словаря.
my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()
print(new_dict)  # {'a': 1, 'b': 2}

fromkeys(iterable, value)
Создает новый словарь с указанными ключами и значением по умолчанию.
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}

get(key, default)
Возвращает значение по указанному ключу, если ключ не найден, возвращает default.
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('c', 0))  # 0

items()
Возвращает представление всех пар "ключ-значение" в виде объектов dict_items.
my_dict = {'a': 1, 'b': 2}
print(my_dict.items())  # dict_items([('a', 1), ('b', 2)])

keys()
Возвращает представление всех ключей в словаре.
my_dict = {'a': 1, 'b': 2}
print(my_dict.keys())  # dict_keys(['a', 'b'])

pop(key, default)
Удаляет элемент с указанным ключом и возвращает его значение. Если ключ не найден, возвращает default.
my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('a')
print(value)  # 1
print(my_dict)  # {'b': 2}

popitem()
Удаляет и возвращает последнюю добавленную пару "ключ-значение". В версиях Python до 3.7 порядок не гарантировался.
my_dict = {'a': 1, 'b': 2}
item = my_dict.popitem()
print(item)  # ('b', 2)

setdefault(key, default)
Возвращает значение по указанному ключу. Если ключ не существует, добавляет его с заданным значением default.
my_dict = {'a': 1}
value = my_dict.setdefault('b', 2)
print(value)  # 2
print(my_dict)  # {'a': 1, 'b': 2}

update(other)
Обновляет словарь, добавляя пары "ключ-значение" из другого словаря или итерируемого объекта.
my_dict = {'a': 1}
my_dict.update({'b': 2, 'c': 3})
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}

values()
Возвращает представление всех значений в словаре.
my_dict = {'a': 1, 'b': 2}
print(my_dict.values())  # dict_values([1, 2])'''