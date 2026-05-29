class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    
    def describe_restaurant(self):
        print(f"餐厅的名字叫{self.restaurant_name}")
        print(f"该餐厅提供的菜系类型是{self.cuisine_type}")
    
    def open_restaurant(self):
        print('The restaurant is opening now!')

rest1 = Restaurant('同庆楼','徽菜')
rest1.open_restaurant()
rest1.describe_restaurant()