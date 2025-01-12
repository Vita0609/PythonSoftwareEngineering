'''str.upper() — возвращает строку в верхнем регистре.
python

"hello".upper()  # "HELLO"
str.lower() — возвращает строку в нижнем регистре.
python

"HELLO".lower()  # "hello"
str.capitalize() — делает первую букву строки заглавной.
python

"hello world".capitalize()  # "Hello world"
str.title() — делает заглавными первые буквы каждого слова.
python


"hello world".title()  # "Hello World"
str.swapcase() — меняет регистр на противоположный.
python


"Hello World".swapcase()  # "hELLO wORLD"
2. Работа с содержимым строки
str.isdigit() — проверяет, состоит ли строка только из цифр.
python


"123".isdigit()  # True
str.isalpha() — проверяет, состоит ли строка только из букв.
python


"abc".isalpha()  # True
str.isalnum() — проверяет, состоит ли строка только из букв и цифр.
python


"abc123".isalnum()  # True
str.isspace() — проверяет, состоит ли строка только из пробелов.
python


"   ".isspace()  # True
str.startswith(prefix) — проверяет, начинается ли строка с подстроки prefix.
python


"hello".startswith("he")  # True
str.endswith(suffix) — проверяет, заканчивается ли строка на suffix.
python


"hello".endswith("lo")  # True
3. Поиск и замена
str.find(sub[, start[, end]]) — возвращает индекс первого вхождения подстроки sub. Возвращает -1, если не найдено.
python


"hello world".find("world")  # 6
str.index(sub[, start[, end]]) — то же самое, что find(), но вызывает ошибку, если подстрока не найдена.
python


"hello world".index("world")  # 6
str.rfind(sub[, start[, end]]) — ищет подстроку с конца строки.
python


"hello world world".rfind("world")  # 12
str.replace(old, new[, count]) — заменяет все вхождения подстроки old на new. Можно указать count для ограничения числа замен.
python


"hello world".replace("world", "Python")  # "hello Python"
4. Разделение и объединение
str.split(sep=None, maxsplit=-1) — разбивает строку на список по разделителю sep.
python


"a,b,c".split(",")  # ["a", "b", "c"]
str.rsplit(sep=None, maxsplit=-1) — разбивает строку с конца.
python


"a,b,c".rsplit(",", 1)  # ["a,b", "c"]
str.splitlines() — разбивает строку на строки по разделителям строк.
python


"a\nb\nc".splitlines()  # ["a", "b", "c"]
str.join(iterable) — объединяет элементы из iterable в строку, используя строку как разделитель.
python


", ".join(["a", "b", "c"])  # "a, b, c"
5. Удаление пробелов и символов
str.strip(chars=None) — удаляет указанные символы (по умолчанию пробелы) с начала и конца строки.
python


"  hello  ".strip()  # "hello"
str.lstrip(chars=None) — удаляет символы только с начала строки.
python


"  hello  ".lstrip()  # "hello  "
str.rstrip(chars=None) — удаляет символы только с конца строки.
python


"  hello  ".rstrip()  # "  hello"
6. Форматирование строк
str.format(*args, **kwargs) — форматирует строку, подставляя значения.
python


"Hello, {}".format("World")  # "Hello, World"
str.zfill(width) — заполняет строку нулями слева до длины width.
python


"42".zfill(5)  # "00042"
str.center(width[, fillchar]) — выравнивает строку по центру, заполняя пустоты символами fillchar.
python


"hello".center(10, "-")  # "--hello---"
str.ljust(width[, fillchar]) — выравнивает строку влево.
python


"hello".ljust(10, "-")  # "hello-----"
str.rjust(width[, fillchar]) — выравнивает строку вправо.
python


"hello".rjust(10, "-")  # "-----hello"
7. Преобразование
str.encode(encoding="utf-8", errors="strict") — кодирует строку в байты.
python


"hello".encode()  # b'hello'
str.casefold() — приводит строку к нижнему регистру для сравнений (более агрессивно, чем lower()).
python


"HELLO".casefold()  # "hello" '''