from pathlib import Path
import json

path = Path('chapter_10/username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"欢迎回来，{username}")
else:
    username = input("请输入您的姓名：")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"您下次登录时，系统仍然会记住您的名字是：{username}")