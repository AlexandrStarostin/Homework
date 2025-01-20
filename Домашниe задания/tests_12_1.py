from unittest import TestCase
from module_12_1 import Runner

class RunnerTest(TestCase):

    def test_walk(self):
        runn = Runner('Sas')

        # print(runn.walk())
        # print(runn.walk())
        # print(runn.walk())
        # print(runn.walk())
        # print(runn.walk())
        # print(runn.walk())
        # print(runn.walk())
        # print(runn.walk())
        # print(runn.walk())
        # print(runn.walk())

        for _ in range(10):
            print(runn.walk())
        self.assertEqual(runn.distance, 50)

    def test_run(self):
        ruun = Runner('Sas')
        for _ in (range(10)):
            print(ruun.run())

        self.assertEqual(ruun.distance, 100)

    def test_challenge(self):
        runn_run = Runner('Dasha')
        for _ in (range(10)):
            print(runn_run.run())
        dis_r = runn_run.distance

        runn_walk = Runner('Masha')
        for _ in (range(10)):
            print(runn_walk.walk())
        dis_w = runn_walk.distance

        self.assertNotEqual(dis_r, dis_w)
