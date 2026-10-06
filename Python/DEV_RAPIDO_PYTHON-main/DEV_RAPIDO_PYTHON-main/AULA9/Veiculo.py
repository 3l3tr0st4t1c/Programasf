from dataclasses import dataclass
from Pessoa import Pessoa
from Marca import Marca

@dataclass
class Veiculo:
        
        placa: int
        cor: str
        proprie_cpf: Pessoa
        marca_id: Marca
        modelo: str