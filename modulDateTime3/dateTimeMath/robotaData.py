'''
                                      ***Работа з датой***
Python содержит инструменты, предназначенные для работы з датой и временем, позволяющие представлять их в формате, понятном пользователям. Вы привыкли к стандартному отображению даты в календарях почты, веб-сайтах и ​​т.д.

Однако в программировании даты выглядят иначе, и для осуществления преобразований между разными форматами в Python используется специальный встроенный модуль datetime. Этот модуль предоставляет классы для манипуляций з датами и временем.

          Основные возможности datetime:
-определение текущей даты и времени;
-вычисление интервала между двумя событиями;
-определение дня недели, высокосного года для любой даты в прошлом не ранее года datetime.MINYEAR или в будущем не позднее года datetime.MAXYEAR;
-сравнение даты и времени нескольких событий з помощью операторов сравнения;
-работа з временными зонами, сравнение событий з учетом временных зон и перехода на летнее/зимнее время;
-преобразование даты/времени в строку и наоборот.

Перед работой з датами и временем необходимо импортировать модуль в нашем скрипте: '''

import datetime
'''Для получения текущей даты и времени используется метод '''
datetime.now()

import datetime
now = datetime.datetime.now()
print(now)

'''Вывод в формате год-месяц-день часа:минуты:секунды.микросекунды:'''
'''2023-12-14 12:39:29.992996'''

'''Работу з модулями мы еще рассмотрим, но объект datetime в свой скрипт мы также можем получить, просто вытащив иго из модуля:'''
from datetime import datetime

'''Да – и модуль и объект имеют одинаковое имя, вы все правильно поняли. 😉'''
'''В результате вызова метода now() мы получаем объект datetime, у которого есть ряд полезных атрибутов:'''
'''
from datetime import datetime
current_datetime = datetime.now()
print(current_datetime.year) Возвращает год даты. Например, если now содержит дату "2023-12-14 12:39:29", now.year будет 2023.
print(current_datetime.month) Возвращает луну как число от 1 до 12. В нашем примере now.month будет 12.
print(current_datetime.day) Возвращает день луны. Для "2023-12-14 12:39:29" now.day будет 14.
print(current_datetime.hour) Возвращает час дня от 0 до 23. В нашем случае now.hour будет 12.
print(current_datetime.minute) Возвращает минуты времени от 0 до 59. Для даты now.minute будет 39.
print(current_datetime.second) Возвращает секунды от 0 до 59. В нашем примере now.second будет 29.
print(current_datetime.microsecond) Возвращает микросекунду времени. Это значение может быть от 0 до 999999. В "2023-12-14 12:39:29.992996", now.microsecond будет 992996.
print(current_datetime.tzinfo) Возвращает информацию о временной зоне объекта datetime. Для now, если временная зона не указана, tzinfo будет None.
'''
'''
У объекта datetime есть методы, чтобы получить дату (без времени) и время (без даты):'''
from datetime import datetime

current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())
# Выведет 2023-12-14
# 12:59:06.709007

'''
Есть обратный метод datetime.combine, который используется для создания нового объекта datetime путем комбинирования объектов date и time. 
Это позволяет создавать точный момент времени, указывая дату и время в отдельности, а затем объединяя их.
Основной синтаксис:'''
datetime.datetime.combine(date_object, time_object)
# date_object: Объект date, содержащий информацию о годе, месяце и дне.
# time_object: Объект time, содержащий информацию о часах, минутах, секундах и микросекундах.
'''Пример'''
import datetime
# Создание объектов date и time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбинирование даты и времени в один объект datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)
print(combined_datetime)  # Виведе "2023-12-14 12:30:15"
'''
В этом примере мы создаем объект date для представления конкретной даты (14 декабря 2023 г.) и объект time для представления конкретного времени (12:30:15). Затем мы используем datetime.combine для создания нового datetime объекта, который представляет этот конкретный момент времени.
Этот метод полезен, когда у вас есть отдельные компоненты даты и времени, которые необходимо объединить для получения точного момента во времени.
Чтобы создать объект datetime з конкретной выбранной датой в Python, можно использовать конструктор класса datetime.datetime, передавая ему год, месяц и день в качестве аргументов. Также можно указать час, минуту, секунду и микросекунду, но это не обязательно – если их пропустить, они будут установлены на 0.'''


'''Для создания объекта datetime з определенной датой:'''
import datetime
# Создание объекта datetime с конкретной датой
specific_date = datetime.datetime(year=2020, month=1, day=7)
print(specific_date) # Выведет "2020-01-07 00:00:00"
# В этом примере создается объект datetime для 7 января 2020 года. 
# Поскольку время не указано, оно автоматически устанавливается на начало дня (00:00:00).

'''Создание объекта datetime з датой и временем'''
import datetime
# Создание объекта datetime с конкретной датой и временем
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)
print(specific_datetime) # Выведет "2020-01-07 14:30:15"
# Здесь создается объект datetime для 7 января 2020 в 14:30:15.
# Использование ключевых параметров помогает избежать путаницы и обеспечивает четкость при указании конкретных компонентов времени.

'''Метод weekday() используется для получения номера дня недели для указанной даты. Он возвращает номер дня недели, где понедельник номер 0, а воскресенье - 6.'''
from datetime import datetime
# Створення об'єкта datetime
now = datetime.now()
# Отримання номера дня тижня
day_of_week = now.weekday()
# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")  # Сьогодні: 3

'''Метод часто используется в сценариях, где требуется определить день недели для определенной даты, например, при создании календарей, планировании событий или вычислениях, связанных с рабочими днями. Он также полезен для установления условий в зависимости от дня недели.

Для сравнения двух объектов datetime в Python, вы можете использовать стандартные операторы сравнения, такие как 
== (равенство), 
!= (неравенство), 
< (меньше), 
> (больше), 
<= (меньше или равно) 
> = (больше или равно). 
Эти операторы позволяют сравнивать даты и времена, чтобы определить, предусматривает ли один объект datetime, наступает или является точно таким же как другой.'''
from datetime import datetime
# Создание двух объектов datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Сравнение дат
print(datetime1 == datetime2) # False, потому что дать не одинаковые
print(datetime1 != datetime2) # True, потому что дать разные
print(datetime1 < datetime2) # True, потому что datetime1 предшествует datetime2
print(datetime1 > datetime2) # False, потому что datetime1 не наступает за datetime2

'''
                 Ключевые аспекты: методы работы з датами и временем в Python:
datetime.now(): Метод возвращает объект datetime, содержащий текущую дату и время.
datetime.date(): Этот метод возвращает объект date, который представляет только дату (без времени).
datetime.time(): Метод возвращает объект time, содержащий только время (без даты).
datetime.combine(date, time): Этот метод используется для объединения объектов date и time и создания нового объекта datetime.
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0): Конструктор класса datetime позволяет создать объект datetime с конкретной датой и временем.
weekday(): Метод определяет номер дня недели для указанной даты, где понедельник имеет номер 0, а воскресенье – 6.'''

'''
       Методы сравнения объектов datetime:
== (равенство): Сравнивает, есть ли две даты равны.
!= (неравенство): Сравнивает, не равны ли две даты.
< (меньше): Определяет, предшествует ли одна дата другой.
> (больше): Определяет, наступает ли одна дата за другой.
<= (меньше или равно): Сравнивает, одна ли дата меньше или равна другой.
>= (больше или равно): Сравнивает, одна ли дата больше или равна другой.'''

'''
                         ***Работа з временными интервалами timedelta***
В модуле datetime есть класс timedelta, который используется для представления разницы между двумя моментами во времени. 
Объекты timedelta могут представлять дни, часы, минуты, секунды и микросекунды. временных интервалов.

Объект timedelta можно создать, задавая недели, дни, часы, минуты, секунды, миллисекунды и микросекунды, передав один или несколько из следующих параметров: days, seconds, microseconds, milliseconds, minutes, hours, weeks. то он равен 0 по умолчанию.'''
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta) # 64 days, 8:05:56.000010

'''Если вычесть из одного datetime объекта другой, то получим timedelta объект.'''
from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0
# Здесь мы с помощью метода total_seconds выполнили конвертацию timedelta в секунды. 

'''Максимальный диапазон для timedelta ограничен примерно 9999 годами, что более чем достаточно для большинства приложений. 
Можно создавать объекты timedelta, чтобы получить дату/время удаленную от исходной.'''
from datetime import datetime, timedelta
now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date) # 2023-12-28 14:08:46.342976

'''Или от какой-то конкретной даты.'''
from datetime import datetime, timedelta

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

'''
Но если нужно производить вычисления или сравнения, основанные на последовательности дат, например, для определения количества дней между двумя датами.
Мы можем использовать метод toordinal(), возвращающий порядковый номер дня, учитывая количество дней с 1 января 1 нашей эры (т.е. с начала христианского календаря). Этот метод превращает объект datetime в целое число, представляющее порядковый номер данного дня.'''
from datetime import datetime

# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")
# Порядковий номер дати 2023-12-18 00:00:00 становить 738872

'''Например, мы хотим определить сколько прошло полных дней, когда Наполеон сжег Москву, а это произошло 14 сентября 1812 года.'''
from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since) # 77161

'''
                                         ***Работа з timestamp***
В контексте программирования и обработки данных термин timestamp (временная метка) используется для указания конкретного момента во времени. 
Это обычно представляется как количество секунд (или миллисекунд/микросекунд в некоторых системах) с определенной начальной даты, чаще всего с 1 января 1970 г. в UTC, это часовой пояс Гринвича. Подробно о самом UTC поговорим немного дальше. Пока timestamp для нас это просто принятая константа и ничего особенного она не значит. Просто для удобства люди когда-то начали отсчитывать время в секундах с этого момента и это оказалось очень удобно. Является стандартным способом представления времени во многих операционных системах и программных языках.

Ведь сравнить два числа всегда легче и быстрее, чем сравнить сложную структуру дат и времен. Вы встретите использование timestamp в программировании, базах данных, логировании событий и сохранении информации о временных моментах событий.

☝ timestamp является универсальным способом представления времени, поскольку оно не зависит от временных зон и календарных систем.
В Python вы можете преобразовать объект datetime в timestamp и наоборот. Конвертация datetime в timestamp'''
from datetime import datetime

# Текущее время
now = datetime.now()
# Конвертация datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp) # Выведет timestamp текущего времени 702854066.56633

'''Конвертация timestamp в объект datetime'''
from datetime import datetime
# Предположим, есть timestamp
timestamp = 1617183600
# Конвертация timestamp обратно в datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object) # Выведет соответствующий datetime 2021-03-31 12:40:00

'''
                                                  ***Парсинг даты из строки***
Когда нужно отобразить дату и время в понятном для человека формате, мы используем метод strftime. Он применяется при записи временных меток в файлы логирования, при отображении даты и времени на веб-страницах или в пользовательских интерфейсах, а также при форматировании дат для сохранения в базах данных.
Таким образом, метод strftime используется для форматирования объектов даты и времени datetime в строки с помощью специфических форматных кодов. Этот метод дает возможность представить дату и время в удобном для чтения формате или в соответствующем специфическим требованиям формате.
Синтаксис метода strftime выглядит следующим образом:'''
datetime_object.strftime(format)
# Где datetime_object – это объект datetime, а format – строка формата, определяющая, как дата и время должны быть представлены.

'''
Каждый код в строке формата начинается с символа % и представляет определенный компонент даты или времени. 

  Вот некоторые из наиболее используемых кодов:
%Y – год с четырьмя цифрами (например, 2023).
%y – год с двумя цифрами (например, 23).
%m – месяц как номер (например, 03 для марта).
%d – день месяца как номер (например, 14).
%H – час (24-часовой формат) (например, 15).
%I - час (12-часовой формат) (например, 03).
%M – минуты (например, 05).
%S – секунды (например, 09).
%A – полное название дня недели (например, Tuesday).
%a – сокращенное название дня недели (например, Tue).
%B – полное название месяца (например, March).
%b или %h – сокращенное название месяца (например, Mar).
%p – AM или PM для 12-часового формата.

Рассмотрим несколько примеров'''
from datetime import datetime

now = datetime.now()

# Форматирование даты и времени
formatted_date = now.strftime("%Y-%m-%d%H:%M:%S") # 2023-12-18 01:37:07
print(formatted_date)

# Форматирование только даты
formatted_date_only = now.strftime("%A, %d %B %Y") # Вторник, 18 Декабря 2023
print(formatted_date_only)

# Форматирование только времени
formatted_time_only = now.strftime("%I:%M %p") # 01:37 AM
print(formatted_time_only)

# Форматирование только даты
formatted_date_only = now.strftime("%d.%m.%Y") # 18.12.2023
print(formatted_date_only)

'''
                                    strptime
Метод strptime в Python используется для преобразования строк в datetime объекты. Этот метод является противоположностью strftime, который преобразует объекты datetime в строки. strptime позволяет анализировать строки, содержащие дату и/или время, и преобразовывать их в структурированные объекты datetime с помощью определенного формата.
Синтаксис метода strptime выглядит следующим образом:'''
datetime_object = datetime.strptime(string, format)
# string - строка, содержащая дату и/или время.
# format – строка формата, указывающая, как разобрать string.
'''Коды форматирования для strptime такие же, как и для strftime. Например, %Y представляет год с четырьмя цифрами, %m - месяц в виде двухзначного числа и т.д.'''
'''Рассмотрим случай когда с веб-сайта есть строка дата "2023.03.14" какого-нибудь поста и нам нужно перед тем как сохранить дату в базе данных превратить ее в объект datetime'''
from datetime import datetime
# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"
# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу 2023-03-14 00:00:00
# В этом примере строка date_string преобразуется в объект datetime с помощью определенного формата: "2023.03.14" это "%Y.%m.%d".
'''С точки зрения применения метод strptime полезен, когда нужно обрабатывать даты и времена, полученные в формате строки, например, из текстовых файлов, пользовательского ввода, веб-запросов или баз данных. Он позволяет превратить эти строки в объекты datetime, которыми уже потом легко манипулировать в коде.'''

'''
                        ***Работа з ISO форматом даты***
Формат даты ISO относится к международному стандарту представления дат и времени, известному как ISO 8601. Этот стандарт создан Международной организацией стандартизации (ISO) и используется для унификации представления даты и времени во всем мире.

Формат даты в ISO 8601 выглядит как "YYYY-MM-DD", где:
YYYY – это год (например, 2023),
MM – месяц (например, 01 для января),
DD – день (например, 31).

Формат времени в ISO 8601 выглядит как "HH:MM:SS", где:
HH – часы (от 00 до 23),
MM – минуты (от 00 до 59),
SS – секунды (от 00 до 59, иногда с дополнительными десятичными частями для микросекунд).

Полное представление даты и времени ISO 8601 объединяет эти два формата с "T" между ними, например "YYYY-MM-DDTHH:MM:SS". 
Это отделяет дату от времени и формат легко отличается от других представлений.

ISO 8601 также поддерживает представление временных зон. Например, "Z" на конце означает UTC (координированное всемирное время), а отклонение от UTC может быть представлено как "+HH:MM" или "-HH:MM". Термин UTC, расшифровывающийся как Всемирное координированное время (англ. Coordinated Universal Time), является основной системой времени, от которой регулируются все временные зоны в мире. Он используется в качестве мирового стандарта времени. Он не меняется с временами года и не подлежит переходу на летнее/зимнее время, в отличие от многих местных временных зон.

Из-за своей универсальности UTC широко используется в международных коммуникациях, авиации, астрономии и других отраслях. 
Локальные временные зоны часто определяются как UTC плюс или минус определенное количество часов.

Модуль datetime предоставляет удобные инструменты для работы с датами и временем в формате ISO 8601. 
Объект datetime можно легко преобразовать в строку формата ISO 8601 с помощью isoformat():'''
from datetime import datetime
# Текущая дата и время
now = datetime.now()
# Конвертация в формат ISO 8601
iso_format = now.isoformat()
print(iso_format) # 2023-12-14T15:43:42.651309

'''Для обратного преобразования строки в формате ISO 8601 в объект datetime можно использовать метод fromisoformat():'''
from datetime import datetime
iso_date_string = "2023-03-14T12:39:29.992996"
# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)
# Виведе об'єкт datetime, що відповідає вказаній даті та часу 2023-03-14 12:39:29.992996

'''
Метод isoweekday() в объекте datetime используется для получения дня недели в соответствии с ISO 8601. Согласно этому стандарту, неделя начинается с понедельника, имеющего значение 1, и заканчивается воскресеньем, имеющим значение 7.'''
from datetime import datetime
# Создание объекта datetime
now = datetime.now()
# Использование isoweekday() для получения дня недели
day_of_week = now.isoweekday()
print(f"Сегодня: {day_of_week}") # Вернет число от 1 до 7, что соответствует дню недели
# В этом примере day_of_week будет содержать число от 1 до 7, где 1 соответствует понедельнику, а 7 – воскресенью. Для четверга вывод будет:
# Сьогодні: 4

'''
Метод isoweekday() полезен в сценариях, где требуется определить конкретный день недели, например, при планировании событий или выполнении действий, зависящих от дня недели. Это может быть особенно полезно в бизнес-логике, оперирующей рабочими и выходными днями.
Также рассмотрим полезный метод isocalendar(), который используется для получения кортежа, содержащего ISO год, номер недели в году и номер дня недели согласно ISO 8601.

Вывод isocalendar() - это кортеж (ISO_год, ISO_неделя, ISO_день_недели), где:
ISO_год – это год в формате ISO.
ISO_неделя – номер недели в году по ISO 8601 (от 1 до 53).
ISO_день_неделя – день недели по ISO 8601, где 1 означает понедельник, а 7 – воскресенье.'''
from datetime import datetime
# Создание объекта datetime
now = datetime.now()
# Получение ISO календаря
iso_calendar = now.isocalendar()
print(f"ISO год: {iso_calendar[0]}, ISO неделя: {iso_calendar[1]}, ISO день недели: {iso_calendar[2]}") # ISO рік: 2023, ISO тиждень: 50, ISO день тижня: 4
# В этом примере iso_calendar будет содержать три значения: ISO год, номер недели и номер дня недели в формате datetime.IsoCalendarDate(year=2023, week=50, weekday=4). Вывод до 14.12.2023 будет:
'''Метод isocalendar() полезен в ситуациях, когда нужно работать с недельными интервалами или рассчитывать даты в формате, широко используемом в бизнес-планировании и логистике.'''

'''
Ключевые аспекты: методы работы с ISO форматом даты
Итак, кратко подытожим использование методов, которые мы только что рассмотрели:
Метод isoformat() используется для конвертации объекта datetime в строку в формате ISO 8601.
Метод fromisoformat() используется для конвертации строки в формате ISO 8601 в объект datetime.
Метод isoweekday() используется для получения дня недели в соответствии с ISO 8601.
Метод isocalendar() используется для получения кортежа, содержащего ISO год, номер недели в году и номер дня недели согласно ISO 8601.'''

'''
                                          ***Работа с временными зонами***
Чтобы вывести дату в формате UTC, это можно сделать, добавив информацию о временной зоне к объекту datetime:'''
from datetime import datetime, timezone

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print(local_now)
print(utc_now)  # Виведе поточний час в UTC 2023-12-14 16:39:33.883454 2023-12-14 14:39:33.883454+00:00

'''Чтобы превратить время из UTC в другую временную зону, вам потребуется определить объект timezone с соответствующим смещением. Например, для преобразования времени UTC в время, соответствующее Восточному часовому поясу США (UTC-5 часов), можно сделать следующее:'''
from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)  # 2023-12-14 09:43:06.778253-05:00

'''Чтобы преобразовать локальное время во время UTC, сначала нужно назначить локальном времени соответствующую временную зону, а затем использовать метод astimezone() для конвертации его в UTC:'''
from datetime import datetime, timezone, timedelta

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC 2023-03-14 10:30:00+00:00
# В этом примере мы создали объект datetime с временной зоной UTC+2 (Киев) и превратили его во время UTC. 

'''Стандарт ISO 8601 также поддерживает временные зоны. В Python это можно сделать, добавив информацию о временной зоне к объекту datetime:
'''
from datetime import datetime, timezone, timedelta

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone) # 2023-03-14T12:30:00+02:00
'''Эти методы в datetime модуле делают работу с ISO форматом простой и эффективной, позволяя легко интегрировать стандартизированное представление дат и времени в Python-программы.'''

'''Ключевые аспекты: методы работы с временными зонами в Python
Итак, мы рассмотрели следующие методы и принципы работы с ними:

Добавление информации о временной зоне к объекту datetime:
Метод astimezone используется для преобразования объекта datetime из одной временной зоны в другую. Например, это может быть использовано для конвертации времени из UTC в другие временные зоны.
Преобразование локального времени во время UTC:

Сначала назначаем локальному времени соответствующую временную зону.
Используем astimezone для конвертации в UTC. Этот подход помогает удобно работать с локальным и всемирным временем.

Форматирование в формате ISO 8601 с временной зоной:

Используем isoformat для получения строки объекта datetime в формате ISO 8601 с временной зоной. Это полезно для представления даты и времени в единственном стандартизированном виде.'''















