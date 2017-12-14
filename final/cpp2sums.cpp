#include <iostream>
// sample data - you can add more
int data[] = {5,3,19,12,15,
              19,33,21,1,5,
              26,7,8,14,18};

int sum(int data[], int size){  
  int sum = 0;
  for(int i = 0; i < size; i++){
    sum += data[i];
  }
  return sum;
}

int sum_odd(int data[], int size){
  int sum = 0;
  for(int i = 0; i < size; i++){
    if(data[i] % 2 == 1){
      sum += data[i];
    }
  }
  return sum;
}

main(){
  std::cout << "Sum of first 5: " << sum(data,5) <<"\n";
  std::cout << "Sum of first 5 odd: "<< sum_odd(data,5) <<"\n";
  
  std::cout << "Sum of first 15: " << sum(data,15) <<"\n";
  std::cout << "Sum of first 15 odd: "<< sum_odd(data,15) <<"\n";
  
}