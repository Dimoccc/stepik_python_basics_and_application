
# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

import re, sys

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\b[Aa]+\b", "argh", line, 1))