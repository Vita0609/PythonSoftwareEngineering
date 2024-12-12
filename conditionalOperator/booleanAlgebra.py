                        # Оператор and (и)
# Оператор and використовується для перевірки, чи обидві умови є істинними. 
# Вираз з and вважається True тільки тоді, коли обидва операнди істинні.

#Наприклад:
a = True and False  # False

#Таблиця істинності для and:

#       A           B          A and B
#     True          True         True
#     True          False         False
#     False         True          False
#     False         False         False

                       # Оператор OR (или)
# Оператор or проверяет, является ли хотя бы одно из условий истинным. 
# Выражение из or считается True, если по крайней мере один из операндов истинен:
a = True or False  # True

# Таблица истинности для or:

#         A           B           A or B
#        True        True         True 
#        True        False        True 
#        False       True         True 
#        False       False        False

                       # Оператор not(нет)
# Оператор not используется для инвертирования истинности операнда.
# Если операнд истинен, not превращает его в ложный, и наоборот:
a = not 2 < 0  # True

# В этом примере, поскольку 2<0 является ложным (False), оператор not превращает его в True.

# Таблица истинности для not:

#     A           not A
#     True        False
#     False       True