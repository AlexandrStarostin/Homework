import threading
import time
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.warrior = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        time.sleep(1)
        day = 0
        for war in range(self.warrior, 0, self.power * -1) :
            if war <= self.power and war > 0:
                time.sleep(1)
                print(f'{self.name} сражался {day+1} день(дня)..., осталось 0 войнов')
                time.sleep(1)
                print(f'{self.name} одержал победу спустя {day+1} дней(дня)!')

                if first_knight.is_alive() is False or second_knight.is_alive() is False:
                    print('Все битвы закончились!')
                    # print(first_knight.is_alive())
                    # print(second_knight.is_alive())
            else:
                time.sleep(1)
                day += 1
                print(f'{self.name} сражался {day} день(дня)..., осталось {war - self.power} войнов')
                time.sleep(1)
            continue

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
# first_knight.join()
time.sleep(1)
second_knight.start()
