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
        self.lock.acquire() # Блокировка других потоков для стабильной работы этого потока
        for i in range(100):
            time.sleep(0.001)
            rand = random.randint(50, 500)
            self.check += rand
            print(f'Пополнение: {rand}. Баланс: {self.check}')
            if self.check < 500:
                self.lock.locked()
                continue

            if self.check >= 500:
                self.lock.locked()
                break
        self.lock.release() # Снятие блокировки других потоков после выполнения этого потока

    def take(self):
        self.lock.acquire()
        for i in range(100):
            time.sleep(0.001)
            rand = random.randint(50, 500)
            print(f"Запрос на {rand}")
            if self.check >= rand:
                time.sleep(0.001)
                self.check -= rand
                print(f"Снятие: {rand}, Баланс: {self.check}")
                continue
                # self.lock.release()
            if self.check < rand:
                time.sleep(0.001)
                print(f"Запрос отклонён, недостаточно средств.")
                break
        self.lock.release()
        print(f"Итоговый баланс: {self.check}")

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th1.join()

th2.start()
th2.join()
