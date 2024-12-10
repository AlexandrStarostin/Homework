def is_prime(func):
    def wrapper(*args):
        orig_res = sum(args)
        if orig_res % 2 == 1:
            print('Простое')
            print(orig_res)
        else:
            print('Составное')
            print(orig_res)
    return wrapper

@is_prime
def sum_three(n, m, x):
    return n + m + x

sum_t = sum_three(2, 4, 5)
print(sum_t)

