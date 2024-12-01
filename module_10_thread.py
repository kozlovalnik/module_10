import time
from datetime import datetime as dt
import threading

def write_words(word_count: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}' + '\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


time1 = dt.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time2 = dt.now()
print('Работа функций ',time2 - time1)

time1 = dt.now()
thread1 = threading.Thread(target=write_words(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words(100, 'example8.txt'))
thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
thread4.start()
thread4.join()

time2 = dt.now()
print('Работа потоков ',time2 - time1)
