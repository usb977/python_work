from pathlib import Path

path = Path('C:/Test/python_work/chapter_10/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(float(pi_string))