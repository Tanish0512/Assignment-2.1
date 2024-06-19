from math import e as e, cos as cos, sin as sin

def secant(f, x1, x2, tol):
    iterations = 0
    while abs(f(x2)) > tol:
        temp = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
        x1 = x2
        x2 = temp
        iterations += 1
    return x2, iterations

def f(x):
    return x**2 - 2


ans = secant(f, -5, 3, 0.001)
print(ans)
