from pathlib import Path

prompt = '请输入您的名字：'
prompt += '\n在任何时候输入q即可退出程序！'

name_str = ''

while True:
    name = input(prompt)
    if name=='q':
        break
    else:
        name_str += f"{name}\n"

path = Path('guest_name.txt')
path.write_text(name_str)