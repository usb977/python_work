from pathlib import Path

path = Path('C:/Test/python_work/chapter_10/pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input('请输入你的生日数字:')
if birthday in pi_string:
    print('你的生日在圆周率前100万个小数中！')
else:
    print('在pi的前100万个小数中，没有你的生日数字！')