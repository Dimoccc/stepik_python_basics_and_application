#https://habr.com/ru/articles/349860/

import re
# print(re.match.__doc__)
# print(re.search.__doc__)
# print(re.sub.__doc__)

# Множество подходящих символов a[abc]c - aac abc acc 
pattern = r"abc"
string = "abcabcabc"
match_object = re.search(pattern, string)

print(match_object) 

# Замена всех сиволов в сулчаем опечатки и схождения символа в множество подходящих символов

pattern = r"a[abc]c"
string = "acc"
match_object = re.match(pattern, string)
print(match_object)

string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)