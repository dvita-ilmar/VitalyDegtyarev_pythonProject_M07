"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №7.5
Домашнее задание по теме "Файлы в операционной системе".
"""

import os, time

# Запуск
if __name__ == '__main__':

    directory = '.' # Задание требуемого пути

    for root, dirs, files in os.walk(directory): # Обход всех директорий и файлов по текущему пути
        print(f'В директории {root}\nнаходятся папки:{dirs}\nи файлы:{files}\nПодробнее об имеющихся здесь файлах:')
        for file in files:# Обход всех файлов в текущей директории
            file_path = os.path.join(root, file) # Получение пути к файлу
            file_size = os.path.getsize(file_path) # Получение размера файла
            file_time = os.path.getmtime(file_path) # Получение времени последнего изменения файла в формате Unix
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time)) # Преобразование в понятное время
            parent_dir = os.path.dirname(file_path) # Получение родительской директории
            print(f'Файл {file} имеет: Путь "{file_path}",Размер "{file_size}" байт, Время изменения "{formatted_time}",'
                  f'Родительскую директорию "{parent_dir}"')
        print('\n')
