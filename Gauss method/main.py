import numpy as np


def input_and_validate():
    valid1 = False
    while not valid1:
        try:
            n = int(input('Enter N (number of unknowns): '))
            valid1 = True

            if n <= 0:
                print('Error!')
                valid1 = False

        except ValueError:
            print('-' * 77)
            print('N must be a number!')
            print('-' * 77)

    given_arr = np.zeros((n, n + 1))
    result_arr = np.zeros(n)

    valid2 = False
    while not valid2:
        try:
            print('Enter Augmented Matrix Coefficients:')
            for i in range(n):
                print(f'{i+1} expression')
                for j in range(n + 1):
                    given_arr[i][j] = float(input('a[' + str(i) + '][' + str(j) + '] = '))

            # Gaussian elimination
            for i in range(n):
                if given_arr[i][i] == 0.0:
                    print('Division by zero detected!')
                    break

                for j in range(i + 1, n):
                    ratio = given_arr[j][i] / given_arr[i][i]

                    for k in range(n + 1):
                        given_arr[j][k] = given_arr[j][k] - ratio * given_arr[i][k]

            # Back substitution
            result_arr[n - 1] = given_arr[n - 1][n] / given_arr[n - 1][n - 1]

            for i in range(n - 2, -1, -1):
                result_arr[i] = given_arr[i][n]

                for j in range(i + 1, n):
                    result_arr[i] = result_arr[i] - given_arr[i][j] * result_arr[j]

                result_arr[i] = result_arr[i] / given_arr[i][i]

            print('\nRequired solution is: ')
            for i in range(n):
                print('X%d = %0.2f' % (i, result_arr[i]), end='\t')

            valid2 = True

        except ValueError:
            print('-' * 77)
            print('The array must consist of only numbers!')
            print('-' * 77)


input_and_validate()
