class WordsFinder:
    def __init__(self, *file):
        self.file = file
        self.file_names = []
        for f in self.file:
            self.file_names.append(f)

    def get_all_words(self):
        self.all_words0 = []
        self.file_name0 = []
        self.all_words = []
        self.file_name = []
        #self.file_name_words = None
        self.file = []
        with open(self.file_names[0], 'r', encoding='Utf-8') as file0:

            for line in file0:
                line_l = line.lower()
                line_r1 = line_l.replace('\n', '')
                line_r2 = line_r1.replace('.', '')
                line_r3 = line_r2.replace('!', '')
                line_r4 = line_r3.replace(',', '')
                line_r5 = line_r4.split(' ')
                for string in line_r5:
                   self.all_words0.append(string)
                print(line_r1)

        self.all_words.append(self.all_words0)
        self.file_name0.append(self.file_names[0])
        self.file_name.append(self.file_name0)


        file_name_words = dict(zip(list(self.file_name[0]), list(self.all_words)))

        print()
        print(file_name_words, end=' ')

    def find(self, word):
        self.word = word.lower()
        all_words0 = self.all_words0
        i_w = []
        if self.word in all_words0:
            index_word = all_words0.index(self.word) + 1
            i_w.append(index_word)
        else:
            i_w.append("Нет такого слова")
        w = dict(zip(self.file_name[0], i_w))
        print()
        print(w, end=' ')

    def count(self, word):
        self.word = word.lower()
        all_words0 = self.all_words0
        count_w = []
        if self.word in all_words0:
            n_c = all_words0.count(self.word)
            count_w.append(n_c)
        else:
            count_w.append("Нет такого слова")
        f = dict(zip(self.file_name[0], count_w))
        print(f, end=' ')

finder2 = WordsFinder('file1.txt')

print()
print(finder2.get_all_words())

print(finder2.find('A'))

print(finder2.count('a'))
