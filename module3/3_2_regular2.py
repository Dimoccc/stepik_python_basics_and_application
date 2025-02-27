import re
# \d	Любая цифра. То же самое, что [0-9]
# \D	Любой символ, кроме цифры. То же самое, что [^0-9]
# \w	Любая буква, цифра и нижнее подчёркивание
# \W	Любой символ, кроме буквы, цифры и нижнего подчёркивания
# \s	Любой пробельный символ (пробел, новая строка, табуляция, возврат каретки и тому подобное)
# \S	Любой символ, кроме пробельного
# \A	Начало строки. То же самое, что ^
# \Z	Конец строки. То же самое, что $
# \b	Начало или конец слова
# \B	Середина слова
# \n, \t\, \r	Стандартные строковые обозначения: новая строка, табуляция, возврат каретки
# [ ] — можно указать множество подходящих символов
# ^ - карет, обозначает либо начало строки, либо инвертирование группы символов. (например: "^[^0-9]" — не-цифра в начале строки).

# Ё не входит в А-Я
#  r"\b[а-яА-ЯёЁ]
#| - или

pattern =r"a[a-c]c"
string = "acc"
match_object = re.match(pattern, string)
print(match_object)

pattern =r"a[a-zA-z]c"
string = "abc, acc, aZc, adc, aBc"
match_object = re.findall(pattern, string)
print(match_object)

pattern =r"a[a-zA-z]c"
string = "abc, acc, aZc, adc, aBc"
match_object = re.findall(pattern, string)
print(match_object)


pattern =r"((abc)|(test|test))"
string = "abc, acc, aZc, adc, aBc"
match_object = re.findall(pattern, string)
print(match_object)

pattern = r"(\w+)-\1"
string = "test-test"
match_object = re.match(pattern, string)
print(match_object)