#include <iostream>

int lone_sum(int a, int b, int c){
    if (a==b and b==c and a==c){
        return  0;
    }
    else if (b==c){
        return a;
    }
    else if(a == c){
        return b;
        }
    else if (a==b) {
        return c;
        }
    else{
        return a + b + c;
    }
}

bool cigar_party(int cigars, bool is_weekend){
    return cigars >= 40 && ( is_weekend || cigars <= 60);
}

int main(){
    std::cout << lone_sum(70,70,70) << "\n";
    std::cout << lone_sum(42,8,42) << "\n";
    std::cout << lone_sum(9,10,21) << "\n";
    std::cout << cigar_party(70,true) << "\n";
    std::cout << cigar_party(70,false) << "\n";
}