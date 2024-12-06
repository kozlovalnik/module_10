from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name: str):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            guest_sitted = False
            for i in range(len(self.tables)):
                if self.tables[i].guest is None:
                    self.tables[i].guest = guest
                    guest.start()
                    guest_sitted = True
                    print(f'{guest.name} сел(-а) за стол номер {self.tables[i].number}')
                    break
            if not guest_sitted:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        free_table = False
        while not free_table or not self.queue.empty():
            for i in range(len(self.tables)):
                if not self.tables[i].guest is None:
                    if not self.tables[i].guest.is_alive():
                        print(f'{self.tables[i].guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {self.tables[i].number} свободен')
                        if not self.queue.empty():
                            self.tables[i].guest = self.queue.get()
                            self.tables[i].guest.start()
                            print(f'{self.tables[i].guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[i].number}')
                        else:
                            self.tables[i].guest = None
                            free_table = True
                else:
                    free_table = True


tables = [Table(number) for number in range(1, 6)]
guests_names = [
                'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                ]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()

