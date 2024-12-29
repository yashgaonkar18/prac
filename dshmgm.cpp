#include <iostream>
#include <cmath>
using namespace std;

float calculateHarmonicMean(int values[], int freq[], int n) {
    float weightedSum = 0, totalFreq = 0;
    for (int i = 0; i < n; i++) {
        weightedSum += freq[i] / values[i];
        totalFreq += freq[i];
    }
    return totalFreq / weightedSum;
}

float calculateGeometricMean(int values[], int freq[], int n) {
    float weightedLogSum = 0, totalFreq = 0;
    for (int i = 0; i < n; i++) {
        weightedLogSum += freq[i] * log(values[i]);
        totalFreq += freq[i];
    }
    return exp(weightedLogSum / totalFreq);
}

int main() {
    int n;
    cout << "Enter the number of values in the series: ";
    cin >> n;

    int values[n], freq[n];

    cout << "Enter the values:\n";
    for (int i = 0; i < n; i++) {
        cout << "Value " << i + 1 << ": ";
        cin >> values[i];
    }

    cout << "Enter the corresponding frequencies:\n";
    for (int i = 0; i < n; i++) {
        cout << "Frequency for value " << values[i] << ": ";
        cin >> freq[i];
    }

    float harmonicMean = calculateHarmonicMean(values, freq, n);
    float geometricMean = calculateGeometricMean(values, freq, n);

    cout << "Harmonic Mean: " << harmonicMean << endl;
    cout << "Geometric Mean: " << geometricMean << endl;

    return 0;
}
