from .woodworking_machine import WoodworkingMachine, Companies
# from .woodworking_machine import Companies


class Lathe(WoodworkingMachine):

    def __init__(self, name="", model="", price=0, power=0, manufacture_company: Companies = None, rpm=0,
                 volume_per_sec=0, blade_name_of_cuter="", step_of_cuter=0, purpose=""):
        super().__init__(name, model, price, power, manufacture_company, rpm, volume_per_sec, purpose)
        self.blade_name_of_cuter = blade_name_of_cuter
        self.step_of_cuter = step_of_cuter

    def __del__(self):
        pass

    def __str__(self):
        return f"\n{super().__str__()}"\
               f"Blades: {self.blade_name_of_cuter}\n"\
               f"Step of cuter: {self.step_of_cuter}\n"

    def slice(self):
        print("Slice,slice,slice,slice,slice,slice,slice,slice!!!")
