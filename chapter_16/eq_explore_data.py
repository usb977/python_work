from pathlib import Path
import json

path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)    #从JSON格式转换为Python对象




