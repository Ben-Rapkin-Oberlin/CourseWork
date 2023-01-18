
#include "readers.h"
#include <array>
#include <string>
#include <iostream>

using namespace std;

int main(int argc, char* argv[]){
    string a=(string) argv[1];
    //std::cout<<a<<"\n";
    array<float, 10> data=train(a);
    for (int i=0; i<10; i++){
        std::cout<<data[i]<<"\n";//<<"..."<<i<<"\n";
    }
}