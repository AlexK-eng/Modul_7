class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding= 'utf-8') as file:
                words = file.read().lower()
                for p_marks in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(p_marks, '')
                all_words[file_name] = words.split()
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_position = {}
        for file_name, words in all_words.items():
            if word in words:
                word_position[file_name] = words.index(word) + 1
        return word_position

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_counts = {}
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        return word_counts


if __name__ == '__main__':

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))

