motorcycles = []            #可直接创建空列表
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0,'ducati')        #使用insert方法可在列表任意位置插入新元素
print(motorcycles)

del motorcycles[0]        #知道元素的位置，可以用del删除
print(motorcycles)

poped_motorcycle = motorcycles.pop()   #无参情况下将列表最后一个元素弹出
print(motorcycles)
print(f"弹出的元素是：{poped_motorcycle}")

first_owned = motorcycles.pop(0)         #有参情况下，删除指定索引处的元素
print(f"The first motorcycle I owned was a {first_owned}.")
print(motorcycles)
print("\n")

motorcycles.append('honda')
motorcycles.append('ducati')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)                       #重新恢复列表元素

motorcycles.remove('ducati')           #根据值来删除列表元素，删除第一次出现的
print(motorcycles)  

