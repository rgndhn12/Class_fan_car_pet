from fan_class import Fan

class TestFan:


    def testing_fan(self):

        first_object = Fan("FAST", 10, "yellow", True )
        second_object = Fan("MEDIUM", 5, "blue", False )

        print(f"The First Fan's speed is {first_object.get_speed()} , radius is {first_object.get_radius()}, color is {first_object.get_color()}, and it is {first_object.on()}")
        print(f"The Second Fan's speed is {second_object.get_speed()} , radius is {second_object.get_radius()}, color is {second_object.get_color()}, and it is {second_object.on()}")

test_fan = TestFan()
test_fan.testing_fan()