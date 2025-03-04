import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.search(r"cat.*cat", line) is not None:
        print(line)
#cat.*cat