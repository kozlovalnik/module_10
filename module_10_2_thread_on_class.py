import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy_cnt = 100
        day_cnt = 0
        while enemy_cnt > 0:
            time.sleep(1)
            day_cnt +=1
            enemy_cnt -= self.power
            print(f'{self.name} сражается {day_cnt}..., осталось {enemy_cnt} воинов.')
        print(f'{self.name} одержал победу спустя {day_cnt} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')


