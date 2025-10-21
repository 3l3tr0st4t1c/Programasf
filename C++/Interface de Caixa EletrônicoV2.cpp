#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <thread>
#include <chrono>

using namespace std;

\\ Área de Geração de Senha e Animação: 

string gerarsenha() {
	srand(time(0));
	string senha = "";
	for (int i = 0; i < 6; i++) {
		senha += to_string(rand() % 10);
	}
	return senha;
}

void animacaoCarregamento(const string& mensagem) {
	cout << mensagem;
	for (int i = 0; i < 3; ++i) {
		cout << ".";
		cout.flush();
		this_thread::sleep_for(chrono::milliseconds(500));
	}
	cout << "\n";
}

\\ Fim da Área de Geração de Senha e Animação.
\\ Área de transferência:

void realizarTransferencia(double &saldo, const string& senhaAtual) {
	string contaDestino, senhaDigitada;
	double valor;

	cout << "Digite o número da conta de destino: ";
	cin >> contaDestino;

	cout << "Digite o valor da transferência: R$";
	cin >> valor;

	cout << "Confirme sua operação digitando sua senha: ";
	cin >> senhaDigitada;

	if (senhaDigitada != senhaAtual) {
		cout << "Senha inválida! Transferência cancelada! \n";
		return;
	}
	
	if (valor > saldo) {
		cout << "Saldo Insuficiente. \n";
		return;
	}

	saldo -= valor;
	cout << "Trasnferência de R$" << valor << "para a conta" << contaDestino << "realizada com sucesso. \n";
}

\\ Fim da Área de Transferência.
\\ Área Principal:

int main() {
	double saldo = (rand() % 9000) + 1000;
	string senhaAtual = gerarSenha();
	time_t tempoGerado = time(0);
	int opcao;

	animacaoCarregamento("Incializando o Sistema Bancário");

	cout << "\n Senha temporária gerada: " << senhaAtual << "\n";
	cout << "** Expirará em 120 segundos ** \n\n";

	do {
		cout <<"———— MENU DO CAIXA ELETRÔNICO ———— \n";
		cout << "1 — Ver saldo\n";
		cout << "2 — Depósitar\n";
		cout << "3 — Sacar\n";
		cout << "4 — Transferir\n"; 
		cout << "5 — Gerar nova senha\n";
		cout << "0 — Sair\n";
		cout << "Escolha uma opção: ";
		cin >> opcao;

	switch (opcao) {
		case 1:
		     cout << "Saldo Atual: R$" << saldo << "\n";
			break;

		case 2: {
			double deposito;
		    	cout << "Digite o Valor do Depósito: R$ ";
			cin >> deposito;
			saldo += deposito;
			cout << "Depósito realizado. \n";
			break;
	}

		case 3: {
			double saque;
			cout << "Digite o valor do saque: R$ ";
			cin >> saque;
			   if (saque <= saldo) {
				saldo -= saque;
				cout << "Saque Realizado com Sucesso. \n";
			   } else {
				cout << "Saldo Insuficiente. \n";
		}
		break;
	}

		case 4: 
		    if (difftime(time(0), tempoGerado) > 120) {
			cout << "Senha Expirada. Gere uma nova.\n";
			  } else {
				realizarTransferencia(saldo, senhaAtual);
			  } 
			break;

		case 5:
		    senhaAtual = gerarSenha();
		    tempoGerado = time(0);
		    cout << "Nova senha gerada: " << senhaAtual << "\n";
			break;

		case 0: 
			cout << "Encerrando Seção. \n";
			  break;

		default:
			cout << "Opção Inválida. \n";
			  break;
	}

	this_thread::sleep_for(chrono::milliseconds(800));
	cout << "\n";


	} while (opcao != 0);

   return 0;

}
\\ Fim da Área Principal.