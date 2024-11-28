class File:
    strings = []
    def __init__(self, file_name, string):
        for i in string:
            self.strings.append(i)
        self.file_name = file_name

    def set_file(self):
        file = open(self.file_name, 'w', encoding='utf-8')
        file_t = file.tell()
        file.write(self.strings[0] + '\n')
        file.close()
        strings_tell.append(file_t)

    def set_file1(self):
        file = open(self.file_name, 'a', encoding='utf-8')
        for i in self.strings[1:]:
            file_te = file.tell()
            strings_tell.append(file_te)
            file.write(i + '\n')
        file.close()

    def set_num(self):
        y = 1
        while y <= len(self.strings):
            num.append(y)
            y += 1

    def get_strin(self):
        for i in num:
            for y in strings_tell:
                num_tell.append((i, y))
                i+=1
            break


        num_tell_str = tuple(zip(num_tell, self.strings))
        print(list(num_tell_str))

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']


inform = File('Text.txt', string = info)

num = []
strings_tell = []
num_tell = []

inform.set_file()
inform.set_file1()
inform.set_num()

print(inform.strings)
print(num)
print(strings_tell)

print()

inform.get_strin()
