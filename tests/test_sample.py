from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel

class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    def test4(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 15Mai2022(sun), 16Mai2022(mon), 17Mai2022(tues) 18Mai2022(wed) 19Mai2022(thur) 20Mai2022(fri) 21Mai2022(sat)"))

    def test5(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 09Mai2022(mon)"))
    
    def test6(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 12Mar2022(sat)"))

    def test7(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 07Nov2021(sun), 08Nov2021(mon), 09Nov2021(tues) 10Nov2021(wed) 11Nov2021(thur) 12Nov2021(fri) 13Nov2021(sat) 14Nov2021(sun)"))

