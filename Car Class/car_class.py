#Dahan, Regine Fae M. Dahan   Car class BSCPE 1-5

# The Car Class

class Car:

# __init__ method

    def __init__(self, year_model, maker, speed = 0):
        
    # Car's year model
        self.__year_model = year_model

    # Cars maker
        self.__maker = maker

    # Car's current speed
        self.__speed = speed


#methods
    #accelerate
    def accelerate(self):
        self.__speed += 5

    #brake
    def brake(self):
        self.__speed -= 5

    #get_speed
    def get_speed(self):
        return self.__speed