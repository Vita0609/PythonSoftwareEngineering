'''
              Паттерны проектирования
Паттерны проектирования (design patterns) — это повторяемые решения общих проблем, с которыми сталкиваются разработчики при проектировании программного обеспечения. Они помогают ускорить разработку и улучшить структуру кода.

Вот несколько популярных паттернов проектирования:

1. Singleton (Одиночка)
Гарантирует, что у класса есть только один экземпляр, и предоставляет глобальную точку доступа к этому экземпляру.

Пример:'''
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True, оба объекта указывают на один экземпляр

'''
2. Factory Method (Фабричный метод)
Определяет интерфейс для создания объекта, но позволяет классам наследникам изменять тип создаваемого объекта.

Пример:'''
class Animal:
    def speak(self):
        raise NotImplementedError()

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())  # Woof
print(cat.speak())  # Meow

'''
3. Observer (Наблюдатель)
Определяет зависимость один ко многим между объектами, так что когда один объект изменяет свое состояние, все зависимые объекты уведомляются и обновляются.

Пример:'''
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        print("State updated")

subject = Subject()
observer = ConcreteObserver()

subject.add_observer(observer)
subject.notify()  # State updated

'''4. Decorator (Декоратор)
Позволяет динамически добавлять функциональность объекту, оборачивая его в другой объект.

Пример:'''
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

coffee = Coffee()
milk_coffee = MilkDecorator(coffee)
sugar_milk_coffee = SugarDecorator(milk_coffee)

print(coffee.cost())  # 5
print(milk_coffee.cost())  # 7
print(sugar_milk_coffee.cost())  # 8

'''5. Strategy (Стратегия)
Позволяет изменять алгоритм поведения объекта во время выполнения, делая его независимым от алгоритма.

Пример:'''
class Strategy:
    def execute(self, a, b):
        raise NotImplementedError()

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b

class Calculator:
    def __init__(self, strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        return self._strategy.execute(a, b)

add_strategy = AddStrategy()
subtract_strategy = SubtractStrategy()

calc = Calculator(add_strategy)
print(calc.calculate(5, 3))  # 8

calc = Calculator(subtract_strategy)
print(calc.calculate(5, 3))  # 2

'''Паттерны проектирования: когда хотите создать гибкую архитектуру, легко расширяемую, поддерживаемую и адаптируемую к изменениям.'''
