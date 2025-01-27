# Итерирование по словарю — это блок кода, который очень часто встречается при программировании, поэтому полезно уметь это делать.

# Сначала следует сказать, что словарь сам по себе – это итерированный контейнер и за ним можно итерироваться в цикле for без необходимости заводить какой-либо внешний счетчик и т.д. 
# Создадим словарь, в котором ключами будут числа, а значениями – числительные на английском:
numbers = {
    1: "one",
    2: "two",
    3: "three"
}
# Теперь давайте просто пройдем словарем в цикле и выведем, что нам возвращает итератор на каждой итерации:
for key in numbers:
    print(key)

# Итерируя по словарю, вы перебираете ключи словаря. 
# Такое же поведение можно получить, используя метод keys, но так вы явно укажете, что хотите перебрать ключи:
for key in numbers.keys():
    print(key)

# Часто необхідно перебрати саме значення словника, для цього скористаємося методом values:
for val in numbers.values():
    print(val)

# Щоб перебрати пари ключ значення словника треба використати метод items. 
# На кожній ітерації ми отримаємо пару (ключ, значення):
for key, value in numbers.items():
    print(key, value)

# Важно помнить, что нельзя делать, пока итерируетесь по словарю: нельзя удалять элементы из словаря, нельзя добавлять элементы в словарь. 
# Но можно перезаписывать значение, если вы итерируетесь по ключам. То же касается и списка - нельзя удалять элементы списка и нельзя добавлять элементы в список во время итераций в цикле.
