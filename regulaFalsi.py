from math import e as e, cos as cos, sin as sin
max_iter = 1000
def regulaFalsi(f, a, b, tol):
    iterations = 0
    while abs(f(b - (f(b) / ((f(b) - f(a)) / (b - a))))) > tol and iterations < max_iter:
        c = b - (f(b) / ((f(b) - f(a)) / (b - a)))
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return b - (f(b) / ((f(b) - f(a)) / (b - a))), iterations

def f(x):
    return x**2 - 2

ans = regulaFalsi(f, -5, 3, 0.001)
print(ans)
