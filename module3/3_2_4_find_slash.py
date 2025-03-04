# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\".

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.search(r"[\\]", line) is not None:
        print(line)