import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.search(r"z(\S){3}z", line) is not None:
        print(line)