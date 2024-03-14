import numpy as np

MAX_ITERATIONS = 1000
message = ""


def user_input():
    n = int(input("Enter matrix size: "))
    print("Enter A matrix:")
    a = np.array([input().strip().split() for _ in range(n)], float)
    print("Enter B vector:")
    b = np.array(input().strip().split(), dtype=float)
    exp = float(input("Enter exp:"))
    return n, a, b, exp


def print_equation_system(n, A, b):
    for i in range(n):
        print(" + ".join([str(A[i, j]) + "*x" + str(j + 1) for j in range(n)]), "=", b[i])


def Jacobi(n, A, b, exp):
    global message
    x = np.zeros(n)
    for iteration in range(MAX_ITERATIONS):
        xx = np.zeros(n)
        for i in range(n):
            x1 = A[i, :i]@ x[:i]
            x2 = A[i, i + 1:]@ x[i + 1:]
            xx[i] = (b[i] - x1 - x2) / A[i, i]

        if np.allclose(x, xx, atol=exp):
            break

        message += "Iteration " + str(iteration + 1) + ": " + str(x) + "\n"
        message += "Difference: " + str(x - xx) + "\n\n"

        x = xx
    return x


def demonstration():
    n, A, b, exp = user_input()
    print("\nEquation system:")
    print_equation_system(n, A, b)
    x = Jacobi(n, A, b, exp)
    print("\nIterations:")
    print(message)
    print("Solution:")
    print(x)


if __name__ == "__main__":
    demonstration()