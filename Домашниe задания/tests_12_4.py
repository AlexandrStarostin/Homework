import logging
from unittest import TestCase
from module_12_4 import Runner

class RunnerTest(TestCase):

    def test_walk(self):

        try:
            runn = Runner('Sas', -7)
            logging.info("'test_walk' выполнен успешно")

        except ValueError as ve:
            print(f'Ошибка введения данных: {ve}')
            logging.warning("Неверная скорость для Runner", exc_info=True)
        else:
            for _ in (range(10)):
                print(runn.walk())
            self.assertEqual(runn.distance, 50)

    def test_run(self):

        try:
            ruun = Runner()
            for _ in (range(10)):
                print(ruun.run())
            logging.info('"test_run" выполнен успешно')
        except TypeError as tr:
            print(f'Ошибка введения данных: {tr}')
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
        else:
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

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, filemode= 'w', filename= 'runner_tests.log',
                        format="%(asctime)s | %(levelname)s | %(message)s")



    # logging.debug('q')
    # logging.info('w')
    # logging.warning('e')
    # logging.error('r')
    # logging.critical('t')