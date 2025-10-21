#include <iostream>
using namespace std;

int main() {
	double num1, num2, soma, sub, multi, d1v;
	int escolha1, escolha2;

//	Interface:

	do {

	cout << "Escolha um número a ser calculado: ";
	cin >> num1;

	cout << "Escolha o segundo número a ser calculado: ";
	cin >> num2;


	cout << "Escolha a operação a ser realizada: \n";
	cout << "1 — Soma \n";
	cout << "2 — Subtração \n";
	cout << "3 — Multiplicação \n";
	cout << "4 — Divisão \n";

	cout << "Digite a opção desejada: ";
	cin >> escolha1;

	cout << endl;


//	Sistema:


	switch (escolha1) {
		  case 1: {
			
			soma = num1 + num2;
			cout << "A soma é: " << soma << endl;
		}
		 break;


		case 2: {
			
			sub = num1 - num2;
			cout << "A subtração é: " << sub << endl;
		}
		 break;


		case 3: {

			multi = num1 * num2;
			cout << "A multiplicação é: " << multi << endl;
		}
		 break;


		case 4:
                if (num2 != 0) {
                    d1v = num1 / num2;
                    cout << "A divisão é: " << d1v << endl;
                } else {
                    cout << "Erro: Divisão por zero!" << endl;
                }
                break;
	default:
		cout << "Opção Inválida. " << endl;
		break;
	}


// 	Repetição:

	cout << "Gostaria de realizar mais uma operação? " << ":\n";
	cout << "1 — Sim. \n";
	cout << "2 — Não. \n";
	cin >> escolha2;
		} while (escolha2 == 1);

	cout << "Calculadora encerrada. " << endl;

 return 0;

}