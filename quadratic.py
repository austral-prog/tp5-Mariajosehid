import math

def roots(a, b, c):
    """Return the roots of a quadratic equation as a string."""
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        r1 = (-b + math.sqrt(discriminant)) / (2*a)
        r2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"({r1}, {r2})"
    elif discriminant == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        return "( )"

def value_y(a, b, c, x):
    """Return the value of y for given a, b, c and x."""
    return a * x**2 + b * x + c

def to_string(a, b, c):
    """Return the quadratic function as a string."""
    # Solo constante
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    # Lineal
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    # Cuadrática sin término lineal
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    # Caso general
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    """Return the derivative of the quadratic function as a string."""
    # Solo constante -> derivada 0
    if a == 0 and b == 0:
        return "f'(x) = 0"
    # Derivada de lineal -> constante
    elif a == 0:
        return f"f'(x) = {b}"
    # Derivada de cuadrática sin término lineal
    elif b == 0:
        return f"f'(x) = {2*a} * X"
    # Caso general
    else:
        return f"f'(x) = {2*a} * X + {b}"