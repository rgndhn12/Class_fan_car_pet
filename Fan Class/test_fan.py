import pyfiglet
import time
import colorama
from colorama import Fore
colorama.init()

from fan_class import Fan

border = "✪" * 90
border_2 = " ☪ " * 30
print(border_2)
print(border)
print(Fore.BLUE+pyfiglet.figlet_format("FAN CLASS",font="arrows"))
print(Fore.LIGHTWHITE_EX+border)
print(border_2)
time.sleep(2)
print(Fore.LIGHTBLUE_EX+("The SPEED, RADIUS, COLOR, and SWITCH of the fans is loading..."))
time.sleep(5)

class TestFan:


    def testing_fan(self):

        first_object = Fan("FAST", 10, "yellow", True )
        second_object = Fan("MEDIUM", 5, "blue", False )

        print(border)
        print(Fore.GREEN+(f"The First Fan's speed is {first_object.get_speed()} , radius is {first_object.get_radius()}, color is {first_object.get_color()}, and is the switch on? {first_object.on()}"))
        print(border)
        time.sleep(5)
        print(Fore.LIGHTCYAN_EX+(f"The Second Fan's speed is {second_object.get_speed()} , radius is {second_object.get_radius()}, color is {second_object.get_color()}, and is the switch on? {second_object.on()}"))
        print(border)

test_fan = TestFan()
test_fan.testing_fan()