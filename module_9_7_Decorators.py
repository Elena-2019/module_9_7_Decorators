def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        for i in range(result // 2):
            if result % (i + 2) != 0:
                continue
            else:
                print('Cоставное')
                return result
        print('Простое')
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
