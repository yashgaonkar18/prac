#include <iostream>
#include <cmath>
using namespace std;

void calcExpected(double expected[], int rowSums[], int colSums[], int grandTotal, int numRows, int numCols)
{
    int index = 0;
    for (int i = 0; i < numRows; ++i)
    {
        for (int j = 0; j < numCols; ++j)
        {
            expected[index++] = (double)(colSums[j] * rowSums[i]) / grandTotal;
        }
    }
}

double chiSquareTest( double observed[], double expected[], int size)
{
    double chiSquare = 0.0;

    for (int i = 0; i < size; ++i)
    {
        if (expected[i] == 0)
        {
            cout << "Expected frequency cannot be zero." <<endl;
            return -1; 
        }
        double difference = observed[i] - expected[i];
        chiSquare += (difference * difference) / expected[i];
    }

    return chiSquare;
}

int main()
{
    int numRows, numCols;
    cout << "Enter the number of rows and columns: ";
    cin >> numRows >> numCols;

    int grandTotal;
    cout << "Enter the grand total: ";
    cin >> grandTotal;

    int rowSums[numRows];
    int colSums[numCols];

    cout << "Enter the row sums: ";
    for (int i = 0; i < numRows; ++i)
    {
        cin >> rowSums[i];
    }

    cout << "Enter the column sums: ";
    for (int j = 0; j < numCols; ++j)
    {
        cin >> colSums[j];
    }

    int size = numRows * numCols;
    double observed[size];
    double expected[size];

    cout << "Enter the observed frequencies: ";
    for (int i = 0; i < size; ++i)
    {
        cin >> observed[i];
    }
    calcExpected(expected, rowSums, colSums, grandTotal, numRows, numCols);
    double chiSquareValue = chiSquareTest(observed, expected, size);
    if (chiSquareValue >= 0)
    {
        cout << "Chi-Square value: " << chiSquareValue <<endl;
    }
    return 0;
}