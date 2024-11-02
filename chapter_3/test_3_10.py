places = ['China','American','India','Austrilia','Japan','Korean']
print("原列表为：")
print(places)
print('\n')

places.append('Singepore')
print("末尾加了新加坡：")
print(places)
print('\n')

places.insert(2,'France')
print("将法国插入第3位：")
print(places)
print('\n')

del places[5]
print("删除日本：")
print(places)
print('\n')

places.pop()
print("删除新加坡：")
print(places)
print('\n')

places.pop(4)
print("删除澳大利亚：")
print(places)
print('\n')

places.remove('American')
print("删除美国：")
print(places)
print('\n')

places.append('Malaysia')
places.sort()
print("按照字母表顺序排序：")
print(places)
print('\n')

places.sort(reverse=True)
print(f"将{len(places)}个国家按照字母表顺序反向排序：")
print(places)
print('\n')
print(sorted(places))
print(sorted(places,reverse=True))

places.reverse()
print(places)


