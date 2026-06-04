from pathlib import Path

# path = Path('chapter_10/pi_digits.txt')
path = Path('C:/Test/python_work/chapter_10/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print('**间隔符**')
    print(line)