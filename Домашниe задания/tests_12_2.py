from unittest import TestCase
from module_12_2 import Tournament, Runner
from pprint import pprint



class TournamentTest(TestCase):
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.name = ('Усэйн', 'Андрей', 'Ник')
        self.speed = (10, 9, 3)


    def tearDownClass(self):
        pprint(self.all_results)

    def test_run(self):
        torn = Tournament(90, self.name)
        print(torn)