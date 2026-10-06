from Pessoa import Pessoa
from datetime import date
from Marca import Marca
from Veiculo import Veiculo

pessoa1 = Pessoa(cpf="15263758005", nome="Lá ele", nasc=date(2004, 6, 20), oculos=True)

marca1 = Marca(id=1, nome="Fiat", sigla="FIA")

veiculo1 = Veiculo(placa="RIO4IO6", cor="Preto", proprie_cpf=pessoa1, marca_id=marca1, modelo="Linea")