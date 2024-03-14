def lu_decomposition(matrix, n):

    lower = [[0 for i in range(n)] for j in range(n)]
    upper = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):

        for k in range(i, n):

            sum = 0

            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            upper[i][k] = matrix[i][k] - sum

        for k in range(i, n):

            if i == k:
                lower[i][i] = 1

            else:
                sum = 0

                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                lower[k][i] = int((matrix[k][i] - sum) / upper[i][i])

    print("Lower Triangular\tUpper Triangular")

    for i in range(n):

        for j in range(n):
            print(lower[i][j], end="\t")
        print("", end="\t\t")

        for j in range(n):
            print(upper[i][j], end="\t")
        print("")


matrix = [[3, -2, -1], [-3, 3, 2], [6, -3, -5]]

lu_decomposition(matrix, 3)
