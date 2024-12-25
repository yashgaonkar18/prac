#include<iostream>
#include <cmath>
using namespace std;
int main(){
    float mean, median, sd, skewness;

    cout << "Enter the standard deviation: ";
    cin >> sd;
    cout << "Enter the mean: ";
    cin >> mean;
    cout << "Enter the median: ";
    cin >> median;

    skewness=3*(mean-median)/sd;
    cout << "Karl Pearson Skewness: " << skewness << endl;
    if(skewness>0&&skewness<3){cout<<"data is positively skewed"<<endl;}
    else if(skewness<0&&skewness>-3){cout<<"data is negatively skewed"<<endl;}
    else{ cout<<"data is symmetric"<<endl;}
  return 0;
}