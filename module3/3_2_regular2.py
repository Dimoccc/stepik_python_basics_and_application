import re

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

