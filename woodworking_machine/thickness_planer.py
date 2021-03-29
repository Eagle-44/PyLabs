from .woodworking_machine import WoodworkingMachine, Companies


class ThicknessPlaner(WoodworkingMachine):

    def __init__(self, name="", model="", price=0, power=0, manufacture_company: Companies = None, rpm=0,
                 volume_per_sec=0, amount_of_barabanes=0, name_of_barabanes="", purpose: str = ""):
        super().__init__(name, model, price, power, manufacture_company, rpm, volume_per_sec, purpose)
        self.amount_of_barabanes = amount_of_barabanes
        self.name_of_barabanes = name_of_barabanes

    def __str__(self):
        return f"\n{super().__str__()}" \
               f"Name of barabanes: {self.name_of_barabanes}\n"\
               f"Amount of barabanes: {self.amount_of_barabanes}\n"

    def grind_down(self):
        print("Grind,grind,grind,grind,grind,grind,grind,grind,grind!!!")
