#include <iostream>
#include <cstdlib>
#include <ctime>
#include <windowns.h>

using namespace std;

//Configuração e Formatação de texto:

void imprimirTextoLento(string texto,
	int atraso = 50) {
		for (char c : texto) {
		cout << c << flush;
		sleep(atraso);
		}
	   cout << endl;
	}

//Área de texto:

void introducao() {

	imprimirTextoLento ("Saude o Imperador no Coliseu Escravo!\n", 60);
		sleep(10000); // 10 segundos

	imprimirTextoLento ("Seu objetivo será sobreviver para ter sua liberdade escravo...\n", 60)
		sleep(10000);
	 
	imprimirTextoLento ("Não se esqueça que terás que obedecer ao imperador...\n", 60)
		sleep(10000);

	imprimirTextoLento ("Desobêdiencia resultará em cruéis punições, desde fome até execução no Coliseu!\n", 60)
		sleep(10000);
	}





































































































}