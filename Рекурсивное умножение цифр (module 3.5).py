def  get_multiplied_digits(number):

    str_number = str(number)
    first = []

    print(*f'<str_number> - {str_number}')
    print(f'<str_number> - {type(str_number)}')
    first.append(int(str_number[0]))
    print(f'Первый знак         <first>      {first}')
    print(f'<first>     -  {type(first[0])}')

    for _ in str_number:
        if len(str_number) < 2:
            return first
        else:
            return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(7098))



