from unittest import TestCase
from module_12_1 import Runner

class RunnerTest(TestCase):

    def test_walk(self):
        runn = Runner('Sas')
        print(runn.walk())
        print(runn.walk())
        print(runn.walk())
        print(runn.walk())
        print(runn.walk())
        print(runn.walk())
        print(runn.walk())
        print(runn.walk())
        print(runn.walk())
        print(runn.walk())
        self.assertEqual(runn.distance, 50)

    def test_run(self):
        ruun = Runner('Sas')
        print(ruun.run())
        print(ruun.run())
        print(ruun.run())
        print(ruun.run())
        print(ruun.run())
        print(ruun.run())
        print(ruun.run())
        print(ruun.run())
        print(ruun.run())
        print(ruun.run())
        self.assertEqual(ruun.distance, 100)

    def test_challenge(self):
        runn_run = Runner('Dasha')
        runn_walk = Runner('Masha')
        print(runn_run.run())
        print(runn_run.run())
        print(runn_run.run())
        print(runn_run.run())
        print(runn_run.run())
        print(runn_run.run())
        print(runn_run.run())
        print(runn_run.run())
        print(runn_run.run())
        print(runn_run.run())
        dis_r = runn_run.distance

        print(runn_walk.walk())
        print(runn_walk.walk())
        print(runn_walk.walk())
        print(runn_walk.walk())
        print(runn_walk.walk())
        print(runn_walk.walk())
        print(runn_walk.walk())
        print(runn_walk.walk())
        print(runn_walk.walk())
        print(runn_walk.walk())
        dis_w = runn_walk.distance

        self.assertNotEqual(dis_r, dis_w)
