class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = self.start - self.step


    def __iter__(self):
        self.pointer = self.start - self.step       # Обнуление счетчика перед циклом
        return self            # Возвращаем ссылку, так как сам объект должен быть итератором


    def __next__(self):

        if self.step == 0:
            print('шаг не может быть равен 0')
            raise StopIteration

        if self.step > 0:
            self.pointer += self.step
            if self.pointer < self.stop:
                return self.pointer
            else:
                raise StopIteration

        if self.step < 0:
            self.pointer -= self.step
            if self.pointer < self.stop:
                return self.pointer
            else:
                raise StopIteration

class StepValueError(ValueError):
    pass



iter2 = Iterator(-5, 16, 2)
iter3 = Iterator(6, 15, 0)
iter4 = Iterator(5, 9, -1)
iter5 = Iterator(-10, 43, 9 )



for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()

