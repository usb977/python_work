from pathlib import Path

path = Path('alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('对不起，没找到对应的文件！')