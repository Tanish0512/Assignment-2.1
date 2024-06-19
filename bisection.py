from math import e as e, cos as cos, sin as sin
max_iter = 100
def bisection(f, a, b, tol):
    iterations = 0
    while abs(f((a + b) / 2)) > tol and iterations < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return (a + b) / 2, iterations

def f(x):
    return x**2 - 2


ans = bisection(f, -5, 3, 0.001)
print(ans)