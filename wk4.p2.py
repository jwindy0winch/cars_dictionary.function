#Primary Car Dictionary Function 
def car_dictionary(manufacturer, model, color, year, **kwargs):
    car_detail = {'Manufacturer': manufacturer, 'Model': model, 'Color': color, 'Year':year}
    car_detail.update(kwargs)
    return car_detail

#Subaru Outback
car1 = car_dictionary('Subaru', 'Outback', 'Blue', 2023, fuel='87 Unleaded Gasoline', tow_package=True)
print("Subaru Outback:")
print(car1)

#Jeep Wrangler
car2 = car_dictionary('Jeep', 'Wrangler', 'Red', 2015, fuel='87 Unleaded Gasoline', four_wheel_drive=True)
print("\nJeep Wrangler:")
print(car2)

#Ferrari LaFerrari
car3 = car_dictionary('Ferrari', 'LaFerrari', 'Ferrari Red', 2013, fuel='97 Premium Unleaded Gasoline', turbocharged_engine=True)
print("\nFerrari LaFerrari")
print(car3)