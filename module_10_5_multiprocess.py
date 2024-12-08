from datetime import datetime as dt
import multiprocessing as mp


filenames = [f'./file {number}.txt' for number in range(1, 5)]

def read_info(name):
    all_data =[]
    with open(name) as f:
        all_data.append(f.readline())

for file in filenames:
    with open(file,'w') as f:
        for i in range(0, 1000):
            f.write(f'строка номер {i}')

#time1 = dt.now()
#for file in filenames:
#    read_info(file)
#time2 = dt.now()
#print(time2 - time1,'Линейный вызов',)

if __name__ == '__main__':
    time1 = dt.now()
    mp.Pool().map(read_info, filenames)
    time2 = dt.now()
    print(time2 - time1,'(многопроцессный)',)
