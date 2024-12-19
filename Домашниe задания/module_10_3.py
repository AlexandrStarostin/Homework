import random
import threading
import time


class Bank:
    check = 0

    def __init__(self):
        self.check = Bank.check
        self.balance = int()
        self.lock = threading.Lock()

    def deposit(self):
        # self.lock.acquire() # Блокировка других потоков для стабильной работы этого потока
        for i in range(100):
            time.sleep(0.001)
            rand = random.randint(50, 500)
            self.check += rand
            print(f'Пополнение: {rand}. Баланс: {self.check}')
            if self.check >= 500 and self.lock.locked():  # и (проверка) заблокированы ли другие потоки
                self.lock.release()  # Снятие блокировки других потоков

    def take(self):
        for i in range(100):
            time.sleep(0.001)
            rand = random.randint(50, 500)
            print()
            print(f"Запрос на снятие: {rand}")
            if self.check >= rand:
                time.sleep(0.001)
                self.check -= rand
                print(f"Снятие: {rand}, Баланс: {self.check}")

            if self.check < rand:
                self.lock.acquire()
                time.sleep(0.001)
                print(f"Запрос отклонён, недостаточно средств.")

        print()
        print(f"Итоговый баланс: {self.check}")


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th1.join()  # который не даст выполнять основную программу пока не завершится поток

th2.start()
th2.join()
