import re

pattern =r"a[ab]+a"
string = "ababa"
match_object = re.match(pattern, string)
print(match_object)
print(re.findall(pattern, string))

pattern =r"((abc)|(test|test)*)"
string = "abctest"
match_object = re.match(pattern, string)
print(match_object)
print(re.findall(pattern, string))
print(match_object.groups())

prog = re.compile(r'(?i)[а-я]+')
print(prog)
# re.compile('(?i)[а-я]+', re.IGNORECASE)

pattern = r"Hello (abc|test)"
string = "Hello abc"
match = re.match(pattern, string)
print(match)
print(match.group(0))
print(match.group(1))

pattern = r"(\w+)-\1" # -\1 первая группа
string = "test-test chow-chow"
match_object = re.match(pattern, string)
print(match_object)
duplicates = re.sub(pattern, r"\1",string)
print(duplicates)
