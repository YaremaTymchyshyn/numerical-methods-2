from math import sin, cos


def simpl_iter_method(x0, y0, exp, max_i):
    f1 = lambda x, y: 2*(x*x) - x*y - 5*x + 1
    f2 = lambda x, y: (1+sin(x-0.5))/2

    f1x = lambda x, y: 0
    f1y = lambda x, y: sin(y)
    f2x = lambda x, y: (cos(x-0.5))/2
    f2y = lambda x, y: 0

    if abs(f1x(x0, y0))+abs(f1y(x0, y0)) >= 1 or abs(f2x(x0, y0))+abs(f2y(x0, y0)) >= 1:
        print("Error! The convergence conditions are not met!")

    xn = x0
    yn = y0
    for n in range(0, max_i):
        x = xn
        y = yn
        yn = f2(xn, yn)
        xn = f1(xn, yn)
        print(f"{n} iteration:")
        print(f"x^({n}) = {x}")
        print(f"y^({n}) = {y}")
        print(" ")

        if abs(xn - x) < exp and abs(yn - y) < exp:
            print(f"Solution:")
            return xn, yn

    print(f"Error! There is no solution with this exp")
    return None


if __name__ == "__main__":
    print(simpl_iter_method(0.7, 0.6, 0.001, 100))