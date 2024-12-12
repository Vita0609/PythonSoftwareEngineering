# В Python работа с датой и временем осуществляется с помощью модуля datetime. 
# Этот модуль предоставляет инструменты для работы с датами, временем и их форматированием. 
# Вот основные моменты, с которыми можно столкнуться при работе с датами в Python:

                                            # Импорт модуля
# Для начала работы с датами и временем, нужно импортировать модуль datetime:
import datetime

                                            # Текущая дата и время
# Для получения текущей даты и времени можно использовать метод datetime.now():
now = datetime.datetime.now()
print(now)  # Выведет текущую дату и время

                                            # Получение текущей даты или времени отдельно
# Дата: Для получения только текущей даты используйте datetime.date():
today = datetime.date.today()
print(today)  # Выведет только текущую дату

# Время: Для получения только текущего времени:
current_time = datetime.datetime.now().time()
print(current_time)  # Выведет текущее время

                                             # Преобразование строки в дату
# Для преобразования строки в объект типа datetime используйте strptime():
date_str = "2024-12-01"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj)  # Выведет дату в формате YYYY-MM-DD 
# Второй аргумент (в данном примере "%Y-%m-%d") указывает формат строки.

                                            # Форматирование даты
# Чтобы вывести дату в нужном формате, можно использовать метод strftime():
formatted_date = now.strftime("%d/%m/%Y")
print(formatted_date)  # Выведет дату в формате день/месяц/год

                                            # Операции с датами
# Модуль datetime позволяет выполнять арифметические операции с датами и временем, например, находить разницу между датами:
date1 = datetime.date(2024, 12, 1)
date2 = datetime.date(2023, 12, 1)
delta = date1 - date2
print(delta.days)  # Выведет количество дней между датами

                                            # Временные интервалы
# Для работы с временными интервалами используется timedelta:
from datetime import timedelta

# Добавление 10 дней
new_date = today + timedelta(days=10)
print(new_date)

# Вычитание времени
new_date = today - timedelta(weeks=2)
print(new_date)

                                            # Работа с временными зонами
# Для работы с временными зонами в Python используется модуль pytz (его нужно установить отдельно). 
# Пример использования:
import pytz
from datetime import datetime

tz = pytz.timezone('Europe/Moscow')
datetime_moscow = datetime.now(tz)
print(datetime_moscow)

