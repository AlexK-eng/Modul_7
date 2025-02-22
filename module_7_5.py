import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):

    for file in files:
        filepath = os.path.join(root,file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Время изменения: {formatted_time},'
              f'Размер: {filesize} байт, Родительская директория: {parent_dir}')
        print(f'--------------------------------------------------------------')