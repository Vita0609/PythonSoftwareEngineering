'''
SOLID — это набор из пяти принципов объектно-ориентированного программирования, разработанный Робертом Мартином (Uncle Bob). Эти принципы помогают писать код, который легко понимать, поддерживать, расширять и тестировать.

Расшифровка SOLID:

1. S — Single Responsibility Principle (Принцип единственной ответственности)
Класс должен иметь только одну причину для изменения. Другими словами, класс должен быть ответственным только за одну задачу.

Пример:'''
class Report:
    def __init__(self, content):
        self.content = content

    def save_to_file(self, filename):  # Нарушение принципа SRP
        with open(filename, 'w') as file:
            file.write(self.content)

# Исправление:
class Report:
    def __init__(self, content):
        self.content = content

class FileManager:
    @staticmethod
    def save_to_file(content, filename):
        with open(filename, 'w') as file:
            file.write(content)

'''
2. O — Open/Closed Principle (Принцип открытости/закрытости)
Классы должны быть открыты для расширения, но закрыты для модификации. Вы должны добавлять новую функциональность через расширение, а не изменяя существующий код.

Пример нарушения:'''
class Discount:
    def apply_discount(self, price, customer_type):
        if customer_type == "VIP":
            return price * 0.8
        elif customer_type == "Regular":
            return price * 0.9
# Исправление:
class Discount:
    def apply_discount(self, price):
        raise NotImplementedError

class VIPDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.8

class RegularDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.9

'''
3. L — Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
Объекты дочерних классов должны заменять объекты родительского класса без изменения поведения программы.

Пример нарушения:'''
class Bird:
    def fly(self):
        pass

class Ostrich(Bird):  # Нарушение LSP, потому что страусы не летают
    def fly(self):
        raise Exception("I can't fly")

# Исправление:
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Ostrich(Bird):
    def move(self):
        print("I run")

'''
4. I — Interface Segregation Principle (Принцип разделения интерфейса)
Клиенты не должны быть вынуждены реализовывать интерфейсы, которые они не используют.

Пример нарушения:'''
class Animal:
    def fly(self):
        pass

    def swim(self):
        pass

    def run(self):
        pass

class Dog(Animal):
    def fly(self):  # Лишний метод
        raise NotImplementedError

    def swim(self):
        print("I swim")

    def run(self):
        print("I run")

# Исправление:
class CanSwim:
    def swim(self):
        pass

class CanRun:
    def run(self):
        pass

class Dog(CanSwim, CanRun):
    def swim(self):
        print("I swim")

    def run(self):
        print("I run")

'''
5. D — Dependency Inversion Principle (Принцип инверсии зависимостей)
Модули верхнего уровня не должны зависеть от модулей нижнего уровня. Оба должны зависеть от абстракций.

Пример нарушения:'''
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL")

class Application:
    def __init__(self):
        self.db = MySQLDatabase()  # Жёсткая зависимость

# Исправление:
class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL")

class Application:
    def __init__(self, db: Database):
        self.db = db

'''Зачем нужен SOLID?
Повышает гибкость и расширяемость кода.
Упрощает поддержку и тестирование.
Уменьшает количество багов при изменении кода.
Упрощает взаимодействие в команде, так как код становится более структурированным.'''