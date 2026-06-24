from pathlib import Path
import json

def get_stored_number(path):
    """读取用户最喜欢的数字"""
    contents = path.read_text()
    number = json.loads(contents)
    return number

def display_favorite_number():
    path = Path('favorite_number.json')
    if path.exists():
        number = get_stored_number(path)
        print(f"我知道你最爱的数字是 {number}.")
    else:
        number = input("请输入您最喜欢的数字：")
        path = Path('favorite_number.json')
        contents = json.dumps(number)
        path.write_text(contents)

display_favorite_number()