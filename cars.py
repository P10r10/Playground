def make_car(manufacturer, model, **car):
    car["manufacturer"] = manufacturer
    car["model"] = model
    return car


my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)
my_car_2 = make_car('subaru', 'impresa')
print(my_car_2)