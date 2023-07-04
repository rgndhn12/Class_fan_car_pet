import pyfiglet
import time
import colorama
from colorama import Fore
colorama.init()

from pet_class import Pet

border = "✪" * 90
border_2 = " ☪ " * 30
print(border_2)
print(border)
print(Fore.LIGHTMAGENTA_EX+pyfiglet.figlet_format(" PET CLASS ",font="banner"))
print(Fore.LIGHTWHITE_EX+border)
print(border_2)
time.sleep(3)

#user's input(name,type,age of the pet)

pet_name = input(Fore.BLUE+(" What's the name of your pet? "))
pet_animal_type = input(Fore.CYAN+(" What's your pet's animal type? "))
pet_age = input(Fore.LIGHTYELLOW_EX+(" What's the age of your pet? ")) 

#object of the pet
pet_object = Pet(pet_name, pet_animal_type, pet_age)
 
#display
print(Fore.GREEN+pyfiglet.figlet_format("The information about your Pet is loading...",font ="bubble" ))
time.sleep(5)
print(border)
print(Fore.BLUE+(" Your pet's NAME is... " +  pet_object.get_name()))
time.sleep(3)
print(Fore.CYAN+(" Your pet's ANIMAL TYPE is... " + pet_object.get_animal_type()))
time.sleep(3)
print(Fore.LIGHTYELLOW_EX+(" Your pet's AGE is... " + pet_object.get_age()))