from pathlib import Path

def count_words(path):
    """计算一个文件大概有多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'对不起，没有找到文件 {path} ！')
    else:
        words = contents.split()
        num_words = len(words)
        print(f" {path} 这本书大约有 {num_words} 个单词！")

file_names = ['alice.txt','siddhartha.txt','moby_dick.txt','little_woman.txt']

for file in file_names:
    path = Path(file)
    count_words(path)