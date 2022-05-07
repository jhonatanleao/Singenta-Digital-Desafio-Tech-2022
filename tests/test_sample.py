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
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 3Mar2009(tue), 6Mar2009(fri), 8Mar2009(sun), 14Mar2009(sat), 17Mar2009(tue), 23Mar2009(mon), 28Mar2009(sat)"))

    def test5(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 3Mar2009(tue), 5Mar2009(thur), 7Mar2009(sat), 8Mar2009(sun), 15Mar2009(sun), 17Mar2009(tue)"))

    def test6(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 16Mar2009(mon), 17Mar2009(tue), 18Mar2009(wed), 19Mar2009(thurs), 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test7(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tue), 18Mar2009(wed), 19Mar2009(thurs), 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test8(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test9(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 12Mar2009(thur), 14Mar2009(sat)"))

    def test10(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 7Mar2009(sat), 8Mar2009(sun), 14Mar2009(sat), 15Mar2009(sun)"))
