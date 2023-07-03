#Dahan, Regine Fae M.    Class Fan    BSCPE 1-5

# The Fan class

class Fan:
    
# Three constants ( SLOW = 1, MEDIUM =2, FAST =3)

    SLOW = 1
    MEDIUM = 2
    FAST = 3

# A constructor that creates a fan 
    def __init__(self, speed, radius, color, on):

# Private int data named "speed"
        self.__speed = speed

# Private bol data named on that specifies whether the fan is on (the default is False)
        self.__on = on
# Private float data named "radius"
        self.__radius = radius

# Private string data named "color"
        self.__color = color

# The getters and setters methods for all four data fields

    def get_speed (self):
        return self.__speed
    
    def set_speed (self, speed):
        self.__speed = speed