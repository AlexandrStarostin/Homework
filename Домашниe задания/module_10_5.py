from multiprocessing import Pool
import datetime

def read_info(names):
    for name in names:
        with open(name, 'r', encoding='UTF-8') as file:

            for line in file:
                all_data.append(line)

all_data = []

filename = [f'./file {number}.txt' for number in range(1, 5)]

# start_time = datetime.datetime.now()
# read_info(filename)
# end_time = datetime.datetime.now()
# t = end_time - start_time
# print(f'{t}сек. (линейный)')

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    with Pool(4) as p:  # в объекте Pool указывается количество рабочих процессов в многопроцессорном режиме
        pol = p.map(read_info, filename)

        end_time = datetime.datetime.now()
        t = end_time - start_time
        print(f'{t}сек. (многопроцессный)')
        print(all_data)
