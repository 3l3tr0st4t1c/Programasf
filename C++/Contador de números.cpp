#include <iostream>
using namespace std;

int main() {
	
	int main() {
    int numero;
    int positivos = 0;
    int negativos = 0;

    for (int i = 0; i < 10; i++) {
        cout << "Digite o número #" << (i + 1) << ": ";
        cin >> numero;

        if (numero > 0) {
            positivos++;
        } else if (numero < 0) {
            negativos++;
        }
        // Se quiser, pode ignorar o zero: ele não entra em nenhum contador
    }

    cout << "Total de números positivos: " << positivos << endl;
    cout << "Total de números negativos: " << negativos << endl;

    return 0;
}