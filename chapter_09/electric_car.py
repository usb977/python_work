from car import Car

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """直接调用父类初始化方法来初始化属性"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print(f"This car has a {self.battery_size}-kWh battery.")