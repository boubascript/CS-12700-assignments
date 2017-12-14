#include <iostream>
#include <string>
using std::cout;
using std::string;
using std::endl;



string piglatinify(string phrase){
    
    return phrase
}

int main(){
    string phrase;
    std::cout << "Pig Latin Translator";
    std::cout << "Phrase to be translated: ";
    std::cin >> phrase;
  
    phrase = piglatinify(phrase);
    cout << "\n Translated: " << phrase << "\n";
    return 0;
  }