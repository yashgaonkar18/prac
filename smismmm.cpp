#include <iostream>
#include <algorithm>
using namespace std;

// Function to calculate mean
double calculateMean(int arr[], int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum / n;
}

// Function to calculate median
double calculateMedian(int arr[], int n) {
    sort(arr, arr + n); // Sort the array
    if (n % 2 == 0) {
        return (arr[n / 2 - 1] + arr[n / 2]) / 2.0; 
    } else {
        return arr[n / 2]; // Middle element
    }
}

// Function to calculate mode
int calculateMode(int arr[], int n) {
    int maxCount = 0, mode = arr[0];
    for (int i = 0; i < n; i++) {
        int count = 1;
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                count++;
            }
        }
        if (count > maxCount) {
            maxCount = count;
            mode = arr[i];
        }
    }
    return mode;
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

    cout << "Mean: " << calculateMean(arr, n) << endl;
    cout << "Median: " << calculateMedian(arr, n) << endl;
    cout << "Mode: " << calculateMode(arr, n) << endl;

    return 0;
}