#include <iostream>

void fizzbuzz(int n){
    for(int i = 1;i <=n;i++){
        if(i % 3 ==0){
            if(i % 5 == 0){
                std::cout << "FizzBuzz\n";
            }
            else{
                std::cout << "Fizz\n";
            }
        }
        else if(i % 5 == 0){
            std::cout << "Buzz\n";
        }
        else{
            std::cout << i << "\n";
        }
    }
}

int main(){
  int num;
  //std::cout << "Fizzbuzz. Enter number : ";
  //std::cin >> num;
  fizzbuzz(100);
}