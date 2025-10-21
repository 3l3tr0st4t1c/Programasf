#include <iostream>
#include <cstdlib>  // Para rand() e srand()
#include <ctime>    // Para time()

using namespace std;

int main() {
    double saldo;
    int escolha;
    double valor;

    // Inicializar o gerador de números aleatórios com o tempo atual
    srand(time(0));

    // Gerar saldo inicial entre 100 e 5000
    saldo = 100 + (rand() % 4901);  // 4901 para dar até 5000

    cout << "Bem-vindo ao caixa eletrônico!\n";
    cout << "Seu saldo inicial é de R$ " << saldo << "\n\n";

    do {
        cout << "Escolha uma operação:\n";
        cout << "1 - Ver saldo\n";
        cout << "2 - Sacar\n";
        cout << "3 - Depositar\n";
        cout << "4 - Sair\n";
        cin >> escolha;

        switch (escolha) {
            case 1:
                cout << "Saldo atual: R$ " << saldo << "\n";
                break;
            case 2:
                cout << "Digite o valor para saque: R$ ";
                cin >> valor;
                if (valor <= saldo) {
                    saldo -= valor;
                    cout << "Saque realizado. Novo saldo: R$ " << saldo << "\n";
                } else {
                    cout << "Saldo insuficiente.\n";
                }
                break;
            case 3:
                cout << "Digite o valor para depósito: R$ ";
                cin >> valor;
                saldo += valor;
                cout << "Depósito realizado. Novo saldo: R$ " << saldo << "\n";
                break;
            case 4:
                cout << "Encerrando operação. Obrigado!\n";
                break;
            default:
                cout << "Opção inválida.\n";
        }

        cout << "\n";

    } while (escolha != 4);

    return 0;
}
