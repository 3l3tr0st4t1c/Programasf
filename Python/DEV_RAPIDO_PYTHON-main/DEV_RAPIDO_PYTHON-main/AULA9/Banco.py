import sqlite3
from pathlib import Path
from typing import Any, ClassVar

from Logger_config import logger
from Marca import Marca
from Pessoa import Pessoa
from Veiculo import Veiculo


class BancoDeDados:
    CAMPOS_PESSOA_PERMITIDOS: ClassVar[frozenset[str]] = frozenset(
        {"nome", "nasc", "oculos"}
    )


    def __init__(self, nome_banco: str = "banco.sqlite") -> None:
        self.caminho_banco = Path(__file__).resolve().parent / nome_banco
        self.conn: sqlite3.Connection | None = None


    def conectar(self) -> None:
        try:
            self.conn = sqlite3.connect(self.caminho_banco)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreing_keys= ON")
            logger.info("Conexão com o banco realizada com sucesso!")

        except sqlite3.Error:
            logger.exception("Erro ao conectar ao banco de dados!")
            raise


    def _obter_conexão(self) -> sqlite3.Connection:
        if self.conn is None:
            raise RuntimeError(
                "Banco de dados não conectado! "
                "Execute conectar() antes de realizar operações!"
            )
        return self.conn


    def criar_tabelas(self) -> None:
        conn = self._obter_conexão()

        try:
            with conn:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Pessoa(
                    cpf TEXT PRMARY KEY,
                    nome TEXT NOT NULL,
                    nasc DATETIME NOT NULL,
                    oculos INTEGER NOT NULL
                        CHECK (oculos IN (0, 1))                   
                    )
                    """
                )

                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Marca(
                    id INTEGER PRMARY KEY,
                    nome TEXT NOT NULL,
                    sigla TEXT NOT NULL                   
                    )
                    """
                )

                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Veiculo(
                    placa TEXT PRIMARY KEY,
                    cor TEXT NOT NULL,
                    proprie_cpf TEXT NOT NULL,
                    marca_id INTEGER NOT NULL,
                    modelo TEXT NOT NULL,

                    FOREIGN KEY (proprie_cpf)
                        REFERENCES Pessoa(cpf)
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT

                    FOREIGN KEY (marca_id)
                        REFERENCES Marca(id)
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT
                    )
                    """
                )

                logger.info("Tabelas ciradas com sucesso!")

        except sqlite3.IntegrityError:
            logger.exception("Erro de integridade durante a criação das tabelas!")
            raise     
        
        except sqlite3.OperationalError:
            logger.exception("Erro operacional durante a criação das tabelas!")
            raise

        except sqlite3.DatabaseError:
            logger.exception("Erro no banco durante a criação das tabelas!")
            raise

        except sqlite3.Error:
            logger.exceprion("Erro geral não especificado no SQLite durante a criação das tabelas!")
            raise