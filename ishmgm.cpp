#include <iostream>
#include <cmath>
using namespace std;

void calculateMidpoints(float midpoints[], int lower[], int upper[], int n) {
    for (int i = 0; i < n; i++) {
        midpoints[i] = (lower[i] + upper[i]) / 2.0;
    }
}

float calculateHarmonicMean(float midpoints[], int freq[], int n) {
    float weightedSum = 0, totalFreq = 0;
    for (int i = 0; i < n; i++) {
        weightedSum += freq[i] / midpoints[i];
        totalFreq += freq[i];
    }
    return totalFreq / weightedSum;
}

float calculateGeometricMean(float midpoints[], int freq[], int n) {
    float weightedLogSum = 0, totalFreq = 0;
    for (int i = 0; i < n; i++) {
        weightedLogSum += freq[i] * log(midpoints[i]);
        totalFreq += freq[i];
    }
    return exp(weightedLogSum / totalFreq);
}

int main() {
    int n;
    cout << "Enter the number of class intervals: ";
    cin >> n;

    int lower[n], upper[n], freq[n];
    float midpoints[n];

    cout << "Enter the lower and upper limits of the class intervals:\n";
    for (int i = 0; i < n; i++) {
        cout << "Class " << i + 1 << " (lower, upper): ";
        cin >> lower[i] >> upper[i];
    }

    cout << "Enter the frequencies of the class intervals:\n";
    for (int i = 0; i < n; i++) {
        cout << "Frequency of class " << i + 1 << ": ";
        cin >> freq[i];
    }

    calculateMidpoints(midpoints, lower, upper, n);

    float harmonicMean = calculateHarmonicMean(midpoints, freq, n);
    float geometricMean = calculateGeometricMean(midpoints, freq, n);

    cout << "Harmonic Mean: " << harmonicMean << endl;
    cout << "Geometric Mean: " << geometricMean << endl;

    return 0;
}
