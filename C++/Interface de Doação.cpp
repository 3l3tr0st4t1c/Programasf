#include <iostream>
using namespace std;

int main() {
    
    int escolha = 0, valor = 0, escolha1 = 0, escolha2 = 0;
    
    cout << "Bem-vindo a interface de doação do programa ********. \n";
do{
    cout << "1 — Para doar R$5,00\n";
    cout << "2 — Para doar R$10,00 \n";
    cout << "3 — Para doar R$15,00 \n";
    cout << "4 — Para doar R$20,00 \n";
    cout << "5 — Para doar outros valores \n";
    cin >> escolha1;
    

        switch (escolha1) {
            case 1: {
                cout << "Obrigado pela Doação. \n";}
            break;
            
            case 2: {
                cout << "Obrigado pela Doação. \n";}
            break;
            
            case 3: {
                cout << "Obrigado pela Doação. \n";}
            break;
            
            case 4: {
                cout << "Obrigado pela Doação. \n";}
            break;
            
            case 5: {
                cout<<"Digite o valor desejado: \n";
                cin >> valor;
                cout << "Obrigado por doar " << valor << endl;}
            break; 
            
    default:;}
   cout << "Gostaria de fazer outra doação? \n";
   cout << "1 — Sim. \n";
   cout << "2 — Não. \n";
   cin >> escolha2; 
   escolha1 = 0;
    } while (escolha2 == 1);

    cout << "Obrigado por doar." << endl;

    return 0;
}