def is_prime(func):
    def wrapper(*args):
        res_p = sum(args)
        if res_p % 2:
            print('Простое')
            print(res_p)
            print()
        else:
            print('Составное')
            print(res_p)
            print()
    return wrapper

@is_prime
def sum_three(n, m, x):
    return n + m + x

sum_t1 = sum_three(19, 1, 1)
sum_t2 = sum_three(20,30,40)
sum_t3 = sum_three(1995, 1, 1)


