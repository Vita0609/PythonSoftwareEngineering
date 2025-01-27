                           # Механизм обработки исключений
# Для обработки исключений существует оператор try…except…. Синтаксически этот оператор начинается с ключевого слова try: (попробовать) и продолжается блоком кода, в котором мы ожидаем, что может произойти ошибка.
# Далее следует блок обработки исключений except (кроме), где можно указать одно или более исключений. Если одно из указанных исключений произойдет, выполнится следующий блок кода.
# Этот блок не обязателен, но чаще всего нужен. Он выполнится, если произойдет указанное исключение (одно из них, если их несколько).
# Если ошибки могут быть разными и обрабатывать их нужно тоже по-разному, то можно добавить несколько блоков except, в каждом указать свою ошибку и что делать, если она произойдет.
# Затем следует необязательный блок, который начинается с ключевого слова else. Этот код выполняется только в том случае, если исключений не произошло.
# Последним следует необязательный блок кода, который начинается с ключевого слова finally, он выполнится в любом случае, независимо от того, были ошибки или нет.
# В нашем примере обработка пользовательского ввода будет выглядеть следующим образом:
val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")

# Исключения в Python – это очень мощный инструмент, часто используемый для управления потоком выполнения, а не только для обработки ошибок. 
# В динамических языках никогда нельзя быть на 100% уверенным в том, что пользователь ввел значение корректного типа или что другое приложение не вернуло None вместо int, например.
# Наивным решением этой проблемы будет повсеместное использование проверок if на корректность вводимого пользователем или другого приложения значения. 
# Более продвинутым, более удобным и прозрачным решением является использование механизма обработки исключений там, где они могут произойти из-за некорректных входных данных.
 
age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")

# Напоминаем, что f-строка – это такой шаблон, который позволяет удобным образом генерировать строку, подставляя результат выполнения выражений в нужное место в шаблоне.   
