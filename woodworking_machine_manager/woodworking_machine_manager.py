from woodworking_machine.woodworking_machine import WoodworkingMachine


class WoodworkingMachineManager:

    def __init__(self, workbenches: list[WoodworkingMachine]):
        self.workbenches = workbenches

    def sort_by_volume(self, reverse=False):
        return sorted(self.workbenches, key=lambda w: w.volume_per_sec, reverse=reverse)

    def sort_by_watts(self, reverse=False):
        return sorted(self.workbenches, key=lambda w: w.power, reverse=reverse)

    def add_new_workbenches(self, workbench: WoodworkingMachine):
        self.workbenches.append(workbench)

    def get_workbench(self, index=0):
        return self.workbenches[index]

    def find(self, key, workbenches: list[WoodworkingMachine] = None):
        return filter(key, workbenches if workbenches else self.workbenches)
