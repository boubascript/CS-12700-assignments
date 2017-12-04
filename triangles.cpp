#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;


std::string line(int l, std::string c){
  string newstr = "";
  for(int i = 0;i < l;i++){
    newstr += c;
  }
  return newstr;
}

std::string rect(int w, int h) {
  string rectstr = "";
  for(int i = 0;i < h;i++){
    rectstr += line(w,"*");
  }
  return rectstr;
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  string tristr = "";
  for(int i = 1;i <= h;i++){
    tristr += line(i,"*") + "\n";
  }
  return tristr;
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  string tristr = "";
  int r = 1;
  int s = 1;
  while(r <=h){
    tristr+= line(h-r," ") + line(s, "*") + "\n";
    r++;
    s+=2;
  }
  return tristr;
}

/*
  *
 **
***
 */
std::string tri3(int h) {
  string tristr = "";
  int r = 1;
  int s = h-1;
  while(r <=h){
    tristr+= line(s," ") + line(r, "*") + "\n";
    r++;
    s--;
  }
  return tristr;
}

int main(){
  cout<< tri1(8)<< endl;
  cout<< tri2(8)<< endl;
  cout<< tri3(8)<< endl;
}

