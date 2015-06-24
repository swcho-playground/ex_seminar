
import re

f = open("test2.csv", 'r')

re_carrot_string = re.compile('<(.*)>.*(\d{3}-\d{3,4}-\d{4})')

for line in f.readlines():
    real_line = line.strip()
    match = re_carrot_string.search(line)
    if match:
        print match.group(1), match.group(2)

f.close()
