#include<iostream>
using namespace std;

int main()
{
    float A[10][10], U[10][10];
    float b[10], x[10], y[10], temp;
    int n, k, i, j;
    cout << "Enter the dimension of the matrix: ";
    cin >> n;

start:
    cout << "Enter elements of the symmetric matrix " << n << "x" << n << ":" << endl;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            cout << "[" << i + 1 << "][" << j + 1 << "] = ";
            cin >> A[i][j];
        }
    }
    cout << endl;
    
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            U[i][j] = 0;
        }
    }

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (A[i][j] != A[j][i])
            {
                cout << "The matrix is not symmetric! Please try again." << endl;
                goto start;
            }
        }
    }

    cout << "Enter elements of the vector b:" << endl;
    for (i = 0; i < n; i++)
    {
        cout << "[" << i + 1 << "] = ";
        cin >> b[i];
    }

    for (int i = 0; i < n; i++)
    {
        temp = 0;
        for (int k = 0; k < i; k++)
        {
            temp = temp + U[k][i] * U[k][i];
        }

        U[i][i] = sqrt(A[i][i] - temp);
        for (j = i; j < n; j++)
        {
            temp = 0;
            for (k = 0; k < i; k++)
            {
                temp = temp + U[k][i] * U[k][j];
            }
            U[i][j] = (A[i][j] - temp) / U[i][i];
        }
    }
    cout << endl;

    cout << "U matrix:" << endl;
    for (i = 0; i < n; i++) 
    {
        for (j = 0; j < n; j++)
        {
            cout << U[i][j] << "\t";
        }
        cout << endl;
    }
    cout << endl;

    cout << "UT matrix:" << endl;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            cout << U[j][i] << "    ";
        }
        cout << endl;
    }

    for (i = 0; i < n; i++)
    {
        temp = 0;
        for (int k = 0; k < i; k++)
        {
            temp = temp + U[k][i] * y[k];
        }
        y[i] = (b[i] - temp) / U[i][i];
    }

    for (i = n - 1; i >= 0; i--)
    {
        temp = 0;
        for (int k = i + 1; k < n; k++)
        {
            temp = temp + U[i][k] * x[k];
        }
        x[i] = (y[i] - temp) / U[i][i];
    }
    cout << endl;

    cout << "Vector x:" << endl;
    for (i = 0; i < n; i++)
        cout << "x" << i << " = " << x[i] << endl;

    cout << endl;

    cout << "Vector y:" << endl;
    for (i = 0; i < n; i++)
        cout << "y" << i << " = " << y[i] << endl;

    return 0;
}