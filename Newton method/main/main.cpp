#include <iostream>
#include <math.h>
using namespace std;

void inverse(double m[2][2])
{
	double det, mm;
	det = m[0][0] * m[1][1] - m[0][1] * m[1][0];
	mm = m[0][0];
	m[0][0] = m[1][1] / det;
	m[1][1] = mm / det;
	mm = m[0][1];
	m[0][1] = -m[1][0] / det;
	m[1][0] = -mm / det;
}

void newton_method(double x, double y)
{
	int i = 0;
	double matrix[2][2], dx, dy, norm;
	do
	{
		double expr1 = ((x * x) + (y * y) - 1);
		double expr2 = (x - (y * y * y) - 0.5);

		matrix[0][0] = (2*x);
		matrix[0][1] = (2*y);
		matrix[1][0] = 1;
		matrix[1][1] = ((-3)*(y*y));

		inverse(matrix);
		dx = -matrix[0][0] * expr1 + -matrix[0][1] * expr2;
		dy = -matrix[1][0] * expr1 + -matrix[1][1] * expr2;

		x = x + dx;
		y = y + dy;

		norm = sqrt(expr1 * expr1 + expr2 * expr2);
		i++;

		cout << "\n#" << i << " iteration" << "\nx = " << x << "\ny = " << y << endl;
	} 
	while (norm >= 0.001);
}

int main()
{
	double x, y;
	cout << "Enter x^(0) = ";
	cin >> x;
	cout << "Enter y^(0) = ";
	cin >> y;

	newton_method(x, y);

	return 0;
}