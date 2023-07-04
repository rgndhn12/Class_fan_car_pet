from car_class import Car

car_object = Car(2019, "Mitsubishi",0)

#call accelerate method five times
for i in range(5):
    #get the current speed
    car_object.accelerate()
    #display
    print(car_object.get_speed())


#call brake method five times
    #get the current speed
    #display