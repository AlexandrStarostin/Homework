import os
import time

os.chdir(r'C:\Users\Саша\PycharmProjects\pythonProject\Домашниe задания\second')

for root, dirs, files in os.walk('.'):

    for file in files:
        f_time = []
        filepath = os.path.abspath(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime('%d-%m-%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
