import threading
import time
import random

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            time.sleep(0.001)
            self.balance += (i := random.randint(50, 500))
            print(f'Пополнение: {i}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for _ in range(100):
            print(f'Запрос на: {(i := random.randint(50, 500))}')
            if i <= self.balance:
                self.balance -= i
                print(f'Снятие: {i}. Баланс: {self.balance}')
            else:
                with self.lock:
                    print('Запрос отклонён, недостаточно средств')

bank = Bank()
thread1 = threading.Thread(target=bank.deposit)
thread2 = threading.Thread(target=bank.take)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f'Итоговый баланс: {bank.balance}')
