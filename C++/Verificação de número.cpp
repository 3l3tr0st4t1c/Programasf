#include <iostream>
using namespace std;

int main() {

	int resto, num1;


	cout << "Digite o número desejado: " << endl;
	cin >> num1;

	resto = num1 % 2;


	if ( resto == 0)
	   cout << "O número é par! " << endl;
	 else 
	   cout << "O número é ímpar! " << endl;

system("pause");

return 0;

}