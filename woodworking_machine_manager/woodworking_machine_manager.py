from woodworking_machine.woodworking_machine import WoodworkingMachine, Companies


class WoodworkingMachineManager:

    def __init__(self, workbenches: list[WoodworkingMachine]):
        self.workbenches = workbenches

    def sort_by_volume(self, reverse=False):
        return sorted(self.workbenches, key=lambda WoodworkingMachine: WoodworkingMachine.volume_per_sec, reverse=reverse)

    def sort_by_watts(self, reverse=False):
        return sorted(self.workbenches, key=lambda WoodworkingMachine: WoodworkingMachine.power, reverse=reverse)

    def add_new_workbenches(self, workbench: WoodworkingMachine):
        self.workbenches.append(workbench)

    def get_workbench(self, index=0):
        return self.workbenches[index]

    def find_by_name_company(self,company_name:Companies, purpose: str = ""):
         for i in self.workbenches:
             if company_name==i.manufacture_company and purpose==i.purpose:
                 print(i)

