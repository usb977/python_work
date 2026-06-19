from pathlib import Path

path = Path('alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('对不起，没找到对应的文件！')
else:
    #计算《爱丽丝漫游仙境》文件大概有多少单词
    words = contents.split()
    num_words = len(words)
    print(f"《爱丽丝梦游仙境》大约有 {num_words} 个单词！")