import unittest
from woodworking_machine_manager.woodworking_machine_manager import WoodworkingMachineManager
from woodworking_machine.woodworking_machine import Companies
from woodworking_machine.lathe import Lathe
from woodworking_machine.thickness_planer import ThicknessPlaner
from woodworking_machine.circular_saw import CircularSaw


class ManagerTest(unittest.TestCase):

    manager = WoodworkingMachineManager([
        Lathe("AR", "1231", 2000, 1000, Companies.Bosch, 9090, 100, "Dbl-1000", 3, "Wood"),
        CircularSaw("JM", "31-12", 1879, 1100, Companies.Bosch, 6666, 70, "Circular Disk 20cm", 10, "Wood"),
        ThicknessPlaner("PL", "7821", 3999, 2125, Companies.Makita, 10000, 85, 2, "Cutter Head", "Wood")
    ])

    def test_sort_by_volume(self):
        self.assertEqual(sorted(ManagerTest.manager.workbenches, key=lambda w: w.volume_per_sec),
                         ManagerTest.manager.sort_by_volume())
        self.assertEqual(sorted(ManagerTest.manager.workbenches, key=lambda w: w.volume_per_sec, reverse=True),
                         ManagerTest.manager.sort_by_volume(True))

    def test_sort_by_power(self):
        self.assertEqual(sorted(ManagerTest.manager.workbenches, key=lambda w: w.power),
                         ManagerTest.manager.sort_by_watts())
        self.assertEqual(sorted(ManagerTest.manager.workbenches, key=lambda w: w.power, reverse=True),
                         ManagerTest.manager.sort_by_watts(True))

    def test_find(self):
        key_find = lambda w: w.manufacture_company == Companies.Bosch
        self.assertEqual(list(filter(key_find,  ManagerTest.manager.workbenches)),
                         list(ManagerTest.manager.find(key_find)))


if __name__ == '__main__':
    unittest.main()
