from pathlib import Path
import json
#
# path=Path('file_pi.txt')
# content=path.read_text()
# content=content.rstrip()
# print(content)
# lines=content.splitlines()
# for line in lines:
#     print(line)

# pi_string=''
# for line in lines:
#     pi_string+=line
# print(pi_string)
# print(len(pi_string))
# path.write_text('1234567890')
# print(content)

# number=[2,3,5,7,11,13]
path=Path('file_pi.txt')
# content=json.dumps(number)
# path.write_text(content)
content=path.read_text()
numbers=json.loads(content)
print(numbers)