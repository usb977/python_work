from pathlib import Path

def read_names(path):
    try:
        contents = path.read_text()
        names = contents.splitlines()
    except FileNotFoundError:
        pass
    else:
        print("\n文件中读取的宠物名称有：")
        for name in names:
            print(f"\t{name}")

file_lists = ['cats.txt','dogs.txt']
for list_item in file_lists:
    path = Path(list_item)
    read_names(path)