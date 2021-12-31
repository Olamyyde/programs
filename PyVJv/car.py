class Car:
    wheels = 2
    def __init__(self, color, model, year) -> None:
        self.color = color;
        self.model = model;
        self.year = year;
        self.__cup = 3;


e = Car("red", "honda", 2019)
print(e.year)

e.wheels = 4

print(f"The car has {e.wheels} wheels")

e.wheels = 5
print(f"The car has {e.wheels} wheels")
print(f"The car has {Car.wheels} wheels")


# print(e._cup)


print(f"The boy had {e._Car__cup} cups")



"""What if you want to control access to an attribute? (i.e getters and setters) 

Use decorator syntax to create py properties
    - @property
    - @name.setter
    - @name.deleter  
                                                    """

class Truck:
    def __init__(self, color, model, year) -> None:
        self.color = color
        self.model = model
        self.year = year
        self.__cup = 3
        self._voltage = 7

    @property
    def voltage(self):
        return self._voltage


    @voltage.setter
    def voltage(self, volts):
        print("Warning: this can cause problems")
        self._voltage = volts
    
    @voltage.deleter
    def voltage(self):
        print("sth fit spoil for the car")
        del self._voltage


cyber = Truck("blue", "Tesla", 2329)
print(f"My car uses {cyber.voltage} volts")

cyber.voltage = 12

del cyber.voltage
# print(f"My car uses {cyber.voltage} volts")





class Clock:
    def __init__(self, hours, minutes) -> None:
        self._hours = hours
        self._minutes = minutes

    @property
    def minutes(self):
        return self._minutes

    def minutes(self, min):
        if min >= 0 and min < 60:
            self._minutes = min


timer = Clock(2, 40)

print(f'The minute value is {timer._minutes}')

timer.minutes = 30
print(f'The minute value is {timer._minutes}')

timer.minutes = 67
print(f'The minute value is {timer.minutes}')





class Vehicle:
    def __init__(self, color, model) -> None:
        self.color = color
        self.model = model

class Car(Vehicle):
    def __init__(self, color, model, year) -> None:
        super().__init__(color, model)
        self.year = year
        self._voltage = 12

s = Car("orange", "ford", 2018)
s._voltage = 23
print(s._voltage)


    



                    