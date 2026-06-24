from pathlib import Path
import json

numbers = [2,3,5,7,11,12]

path = Path('chapter_10/numbers.json')
contents = json.dumps(numbers)        #转换为JSON格式字符串
path.write_text(contents)             #写入内容