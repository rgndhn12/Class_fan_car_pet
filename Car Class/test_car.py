import pyfiglet
import time
import colorama
from colorama import Fore
colorama.init()

from car_class import Car

border = "✪" * 90
border_2 = " ☪ " * 30
print(border_2)
print(border)
print(Fore.LIGHTYELLOW_EX+pyfiglet.figlet_format(" THE CAR CLASS ",font="avatar"))
print(Fore.LIGHTWHITE_EX+border)
print(border_2)
time.sleep(3)


car_object = Car(2019, "Mitsubishi",0)

#call accelerate method five times
print(Fore.GREEN+pyfiglet.figlet_format("CAR's accelerating..", font ="bell"))
time.sleep(5)

for i in range(5):
    #get the current speed
    car_object.accelerate()
    #display
    print(border)
    print(car_object.get_speed())
    print(border_2)
    time.sleep(2)

#call brake method five times
print(Fore.RED+pyfiglet.figlet_format("CAR's braking...", font ="bell"))

for i in range(5):
    #get the current speed
    car_object.brake()
    #display
    print(border)
    print(car_object.get_speed())
    print(border_2)
    time.sleep(2)