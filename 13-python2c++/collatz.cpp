#include <iostream>

int collatz(int n){
  if(n % 2 == 0){
    n /= 2;
  }
  else{
    n = 3 * n + 1;
  }
  return n;
}

int main(){
  int num;
  std::cout << "Collatz. Enter number : ";
  std::cin >> num;

  while(num > 1){
    num = collatz(num);
    std::cout << num << "\n";
  }
  std::cout << "done\n" ;
  return 0;
}