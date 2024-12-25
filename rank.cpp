#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int arr1[20], arr2[20], arr3[20], arr4[20], n, apple, nn;
    float mango=0.0, rankss;
    cout<<"enter number of elements"<<endl;
    cin>>n;

    cout<<"enter elements of 1st observation table"<<endl;
    for(int i=0;i<n;i++){
        cin>>arr1[i];
    }

    cout<<"enter elements of 2nd observation table"<<endl;
    for(int i=0;i<n;i++){
        cin>>arr2[i];
    }
    cout<<"enter ranks of 1st observation table"<<endl;
    for(int i=0;i<n;i++){
        cin>>arr3[i];
    }

    cout<<"enter ranks of 2nd observation table"<<endl;
    for(int i=0;i<n;i++){
        cin>>arr4[i];
    }

    for(int i=0;i<n;i++){
        apple=arr3[i]-arr4[i];
        mango=mango+(1.0*apple*apple);
    }
    nn=n*n;
    rankss= 1- ((6.0*mango)/(n*(nn-1)));
    cout<<"rank correlation using Spearman's coefficient="<<rankss<<endl;
}