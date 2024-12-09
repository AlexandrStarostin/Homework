def is_prime(func):
    def wrapper(*args):
        orig_res = str(sum(args))
        if len(orig_res) <=1:
            print('Простое')
        else:
            print(sum(args))
    return wrapper

@is_prime
def sum_three(n, m, x):
    return n + m + x


print(sum_three(2, 6,1))
