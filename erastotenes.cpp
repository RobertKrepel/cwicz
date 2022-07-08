#include <iostream>
using namespace std;
int main() {
    int n;
    cout<<"n=";cin>>n;
    bool pierwsze[n];
    pierwsze[2]=true;
    for (int i=3;i<n;i++)
        pierwsze[i]=(i%2==1);
    int d=3;
    while (d*d<n)
    {
        for (int i=d;i*d<n;i+=2)
            pierwsze[i*d]=false;
        do
            d+=2;
        while (!pierwsze[d]);

    }
    cout<<"liczby pierwsze mniejsze od "<<n<<": "<<endl;
    for (int i=2;i<n;i++)
        if (pierwsze[i])
            cout<<i<<" ";
}
