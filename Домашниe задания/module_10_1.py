import threading
import time

def write_words(word_count, file_name):
    word_count = int(word_count)
    with (open(file_name, 'w', encoding='utf-8') as file):
        for word_num in range(1, word_count + 1):
            time.asctime()
            time.sleep(0.1)
            file. write(f"{word_c}  №{word_num}\n")
            continue
        print(f"Завершилась запись в файле {file_name}")


word_c = 'Привет'


wr_1 = write_words(10, 'example1.txt')
wr_2 = write_words(10, 'example2.txt')
wr_3 = write_words(20, 'example3.txt')
wr_4 = write_words(10, 'example4.txt')
#
rt =threading.currentThread()
rt.start()
rt.join()


thr_0 = threading.Thread(target=write_words(7, 'example5.txt'))
thr_0.start()
thr_1 = threading.Thread(target=write_words(2, 'example6.txt'))
thr_1.start()
thr_2 = threading.Thread(target=write_words(40, 'example7.txt'))
thr_2.start()
thr_3 = threading.Thread(target=write_words(7, 'example8.txt'))
thr_3.start()
print(threading.enumerate())


