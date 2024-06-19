from math import e as e, cos as cos, sin as sin
max_iter = 1000
def newtons(f, derf, x, tol):
    iterations = 0
    while abs(f(x)) > tol and iterations < max_iter:
        x = x - f(x) / derf(x)
        iterations += 1
    return x, iterations


def f(x):
    return x ** 2 - 2

def derf(x):
    return 2 * x

result = []
result.append(newtons(f, derf, -5, .001))
print(result)