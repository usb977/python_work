def make_car(brand, model , **car_info):
    car_info['brand_name'] = brand
    car_info['model_name'] = model
    return car_info

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)