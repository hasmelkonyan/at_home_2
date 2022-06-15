

# exercise 1.11
# f(n) = n, եթե n < 3
# f(n) = f(n - 1) + f(n - 2) + f(n - 3), եթե n >= 3


def f_tail_rec(n):
    """tail recursion
    """
    if n < 3:
        return n
    else:
        return f_tail_rec(n - 1) + f_tail_rec(n - 2) + f_tail_rec(n - 3)


print(f_tail_rec(6))


def f_iter(n):
    num0, num1, num2 = 1, 2, 3
    if n < 3:
        return n
    else:
        while n > 3:
            num0, num1, num2 = num1, num2, num0 + num1 + num2
            n -= 1
    return num2


print(f_iter(6))


# exercise 1.12
def pascal_triangle(row, column):
    if row == 0 or column == 0:
        return 1
    elif row == column:
        return 1
    elif column > row:
        return 0
    else:
        return pascal_triangle(row - 1, column) + pascal_triangle(row - 1, column - 1)


print(pascal_triangle(5, 2))


# exercise 1.13
# b^n = (b^(n/2))^2, եթե n-ը զույգ է
# b^n = b * b^(n-1), եթե n-ը կենտ է

def max_pow_iter(m, n):
    res = 1
    if n == 0:
        return res
    elif n == 1:
        return m
    else:
        while n > 1:
            if n % 2 == 0:
                res *= m * m
                n /= 2
            else:
                res *= m
                n -= 1
        return res

print(max_pow_iter(5, 3))


# exercise 1.14
def double(num):
    return num + num


def halve(num):
    if num % 2 == 0:
        return num / 2


# 7 * 10 = 14 * 5
def mul(a, b):
    """this function returns a times b
    """
    if b == 0:
        return 0
    else:
        while b > 0:
            if b % 2 == 0:
                return mul(double(a), halve(b))
            else:
                return a + mul(a, b - 1)



print(mul(30, 1000))








