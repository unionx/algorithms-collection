#!/usr/bin/env python
from sympy import Symbol, solve, limit, oo, sqrt


def solve_fn():
    x = Symbol('x')
    y = Symbol('y')
    result = solve([x+y-1, 3*x+2*y-5], [x, y])
    print(result)


def calc_limit():
    x = Symbol('x')
    result = limit(x*(sqrt(x**2+1)-x), x, oo)
    print(result)


def calc_integrate():
    pass


if __name__ == '__main__':
    calc_limit()
