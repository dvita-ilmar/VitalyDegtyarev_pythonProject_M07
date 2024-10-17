"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №7.3
Домашнее задание по теме "Оператор "with".
"""
from logging import setLogRecordFactory


class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args) # Список имен файлов

    def get_all_words(self):
        all_words = {} # Список всех слов всех файлов
        symbols = (',', '.', '=', '!', '?', ';', ':', ' - ') # Список удаляемых символов
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower() # Приведение строки к нижнему регистру
                    line = ''.join([c for c in line if c not in symbols]) # Исключение символов symbols
                    if all_words.get(file_name, False) is False: # если в словаре нет такого ключа
                        all_words[file_name] = line.split() # добавляем его и помещаем туда список с одним значением
                    else:  # если такой ключ уже есть
                        for word in line.split(): # по-словно (иначе возникает вложенность списков)
                            all_words[file_name].append(word) # добавляем значение в конец списка
        return all_words

    def find(self, word):
        word = word.lower() # Приведение слова к нижнему регистру
        find_words = {} # Словарь найденных слов
        for name, words in self.get_all_words().items():
            found = False # Флаг найденного слова в текущем файле
            for index, current_word in enumerate(words):
                if word == current_word:
                    find_words[name] = index + 1
                    found = True
                    break
            if not found:
                find_words[name] = 'not found'
        return find_words

    def count(self, word):
        word = word.lower()  # Приведение слова к нижнему регистру
        count_words = {} # Словарь количества найденных слов
        for name, words in self.get_all_words().items():
            found = False  # Флаг найденного слова в текущем файле
            count_words[name] = 0
            for current_word in words:
                if word == current_word:
                    count_words[name] += 1
                    found = True
            if not found:
                count_words[name] = 'not found'
        return count_words


# Запуск
if __name__ == '__main__':

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
    print(finder2.find('нет'))  # 'not found'
    print(finder2.count('НеТ')) # 'not found'

    # Проверено с: (совпадение результатов 100%)
    '''
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
    '''