from woodworking_machine_manager.woodworking_machine_manager import WoodworkingMachineManager
from woodworking_machine.lathe import Lathe
from woodworking_machine.circular_saw import CircularSaw
from woodworking_machine.thickness_planer import ThicknessPlaner
from woodworking_machine.woodworking_machine import Companies


class Example:

    def start(self):
        manager = WoodworkingMachineManager([
            Lathe("AR", "1231", 2000, 1000, Companies.Bosch, 9090, 100, "Dbl-1000", 3, "Wood"),
            CircularSaw("JM", "31-12", 1879, 1100, Companies.Bosch, 6666, 70, "Circular Disk 20cm", 10, "Wood"),
            ThicknessPlaner("PL", "7821", 3999, 2125, Companies.Makita, 10000, 85, 2, "Cutter Head", "Wood")
        ])
        print("Sorting by Power:")
        print("".join([str(i) for i in manager.sort_by_watts(True)]))

        print("Sorting by Volume:")
        print("".join([str(i)for i in manager.sort_by_volume(False)]))
        print("Search by Company name and Purpose:")
        for i in manager.find(lambda w: w.manufacture_company == Companies.Bosch,
                              manager.find(lambda w: w.purpose == "Wood")):
            print(i)
