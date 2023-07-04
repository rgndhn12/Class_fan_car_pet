#Dahan, Regine Fae M.   Pet Class  BSCPE 1-5

# The Pet Class
class Pet:

#__init__method
    def __init__(self, name, animal_type, age):

    #Pet's name
        self.__name = name
    #Pet's type
        self.__animal_type = animal_type
    #Pet's age
        self.__age = age

#methods
    #set_name
    def set_name(self,name):
        self.__name = name

    #set_animal_type
    #set_age
    #get_name
    def get_name(self):
        return self.__name
    #get_animal_type
    #get_age

#object of the class
    #user's input(name,type,age of the pet)
    #display