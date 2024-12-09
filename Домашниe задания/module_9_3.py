first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_r = zip(first, second)
firs = list(first_r)
first_result =((len(i[0]) - len(i[1])) for i in firs if not len(i[0]) == len(i[1]))

print(list(first_result))


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

second_result = ((len(first[x]) == len(second[x])) for x in range(len(first)) and range(len(second)))
print(list(second_result))
