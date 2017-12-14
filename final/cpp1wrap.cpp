#include <iostream>

//helper function for me
int smallest(int a,int b, int c){
  int small;
  if(a < b){
    small = a;
  }
  else{
    small = b;
  }
  if(c < small){
    small = c;
  }
  return small;
}

// add your code here
int paper_needed(int l, int w, int h){
  return 2*l*w + 2*w*h + 2*h*l + smallest(l*w, w*h, h*l);
}

int ribbon_needed(int l, int w, int h){
  int smaller,small;
  smaller = smallest(l,w,h);
  if(l == smaller){
      small = std::min(w,h);
  }
  else if(w ==smaller){
      small = std::min(l,h);
  }
  else{
    small = std::min(l,w);
  }
  return 2*smaller + 2 *small + 5;
}

int main(){
  // add your code to test things here
  std::cout << "Paper Needed: " << paper_needed(5,8,3)<< "\n";
  std::cout << "Ribbon Needed: " << ribbon_needed(8,3,5)<< "\n";

  return 0;
}