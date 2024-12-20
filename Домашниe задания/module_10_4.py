import random
import  time
from threading import Thread
from queue import Queue

class  Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        waiting_time = random.randint(3, 10)
        return time.sleep(waiting_time)

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        # print(guests)
        for i in range(len(guests)):
            if i < len(self.tables):
                table = self.tables[i]
            guest = guests[i]
            if table.guest is None:
                table.guest = guest
                guest.start()
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while self.queue.qsize() != 0:
            for table in  self.tables:
                if not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
            if self.queue.qsize() != 0:
                for table in self.tables:
                    if table.guest is None:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-а) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()