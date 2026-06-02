class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    
    def describe_restaurant(self):
        print(f"餐厅的名字叫{self.restaurant_name}")
        print(f"该餐厅提供的菜系类型是{self.cuisine_type}")
    
    def open_restaurant(self):
        print('The restaurant is opening now!')

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['草莓味','香草味','巧克力味']
    def describe_flavor(self):
        for flavor in self.flavors:
            print(f'冰淇淋的口味有：{flavor}')

stand = IceCreamStand('巧乐兹','甜点')
stand.describe_restaurant()
stand.describe_flavor()