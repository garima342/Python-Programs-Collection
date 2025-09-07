#include<iostream>
using namespace std;

int main(){
    int arr[5]= {3,6,8,9,12};
    int max=0;
    int min=0;
    for(int i=0; i<5; i++){
        if (arr[i]>max){
            max=arr[i];
        }
        if (arr[i]<min || min==0){
            min = arr[i];
        }
    }
    cout<<"Max: "<<max<<endl;
    cout<<"Min: "<<min<<endl;
    system("pause");
    return 0;
}