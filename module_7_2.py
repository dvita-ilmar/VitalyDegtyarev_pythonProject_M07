"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №7.2
Домашнее задание по теме "Позиционирование в файле".
"""

def custom_write(file_name, strings):
    res = {}
    file = open(file_name, 'w', encoding='utf-8')
    for index, line in enumerate(info):
        res[(index+1, file.tell())] = line
        file.write(line + '\n')
    file.close()
    return res


# Запуск
if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)