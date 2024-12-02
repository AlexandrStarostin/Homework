def min_i(x):
    a = min(x)
    return a

def max_i(x):
    s = max(x)
    return s

def len_i(x):
    d = len(x)
    return d

def sum_i(x):
    f = sum(x)
    return f

def sorted_i(x):
    g = sorted(x)
    return g


def apply_all_func(int_list, *functions):
    fun = []
    results = []
    for function in functions:
        results.append(function(int_list))
        fun.append(function.__name__)
    return dict(zip(fun, results))


h = 4, 5, 75, 34, 1

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
