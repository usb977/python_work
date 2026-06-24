from pathlib import Path
import json

path = Path('chapter_10/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)  #从JSON格式转换为Python对象

print(numbers)