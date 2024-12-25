#include <iostream>
#include <cmath>
using namespace std;

float calculateHarmonicMean(int arr[], int n) {
    float sum = 0;
    for (int i = 0; i < n; i++) {
        sum += 1/arr[i];
    }
    return n/sum;
}
float calculateGeometricMean(int arr[], int n) {
    float sum = 0;
    for (int i = 0; i < n; i++) {
        sum += log(arr[i]);
    }
        return exp(sum/n);
}

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    int arr[n];
    cout << "Enter the elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout<<"Harmonic Mean : " <<calculateHarmonicMean(arr, n) << endl;
    cout <<"Geometric Mean : "<< calculateGeometricMean(arr, n) << endl;
   
    return 0;
}