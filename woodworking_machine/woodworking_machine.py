from enum import Enum


class Companies(Enum):
    Bosch = 0
    Makita = 1
    Arsenal = 2
    DniproM = 3


class WoodworkingMachine:

    def __init__(self, name="", model="", price=0.0, power=0, manufacture_company: Companies = None, rpm=0,
                 volume_per_sec=0, purpose: str = ""):
        self.name = name
        self.model = model
        self.price = price
        self.manufacture_company = manufacture_company
        self.power = power
        self.rpm = rpm
        self.volume_per_sec = volume_per_sec
        self.purpose = purpose

    def __del__(self):
        pass

    def __str__(self):
        return f"Name: {self.name}\n"\
               f"Model: {self.model}\n"\
               f"Price: {self.price}$$$\n"\
               f"Manufacturer: {self.manufacture_company}\n"\
               f"Power: {self.power} Watts\n"\
               f"Revolutions: {self.rpm} min.\n"\
               f"Volume of processing/sec: {self.volume_per_sec} Cube/m\n"


    def turn_on(self):
        print("On")

    def turn_off(self):
        print("Off")





