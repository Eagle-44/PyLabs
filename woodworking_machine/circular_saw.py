from .woodworking_machine import WoodworkingMachine, Companies


class CircularSaw(WoodworkingMachine):
    def __init__(self, name="", model="", price=0, power=0, manufacture_company: Companies = None, rpm=0,
                 volume_per_sec=0, blade_name_of_circular_saw="", amount_of_blades=0, purpose: str = ""):
        super().__init__(name, model, price, power, manufacture_company, rpm, volume_per_sec, purpose)
        self.blade_name_of_circular_saw = blade_name_of_circular_saw
        self.amount_of_blades = amount_of_blades

    def __str__(self):
        return f"\n{super().__str__()}" \
               f"Name of barabanes: {self.blade_name_of_circular_saw}\n" \
               f"Amount of barabanes: {self.amount_of_blades}\n"

    def cut(self):
        print("Cut,cut,cut,cut,cut,cut,cut,cut,cut,cut!!!")
