CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    senha_hash VARCHAR(255) NOT NULL, 
CONSTRAINT chk_senha_tamanho CHECK (CHAR_LENGTH(senha_hash) >=8),
    email_login VARCHAR(255) UNIQUE
);

CREATE TABLE Artigo (
    id_artigo INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    conteudo LONGTEXT, 
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

CREATE TABLE Resumo (
    conteudo LONGTEXT,
    data_criacao DATETIME NOT NULL,
    id_resumo INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

CREATE TABLE Arquivo (
    tipo VARCHAR(255) NOT NULL,
    data_envio DATETIME NOT NULL,
    id_envio INT NOT NULL,
    id_arquivo INT PRIMARY KEY AUTO_INCREMENT,
    caminho_arquivo VARCHAR(255) NOT NULL, 
    FOREIGN KEY (id_envio) REFERENCES Envia_Arquivos(id_envio) ON DELETE CASCADE
);

CREATE TABLE Comentario (
    texto LONGTEXT,
    data_postagem DATETIME NOT NULL,
    id_artigo INT,
    FOREIGN KEY (id_artigo) REFERENCES Artigo(id_artigo) ON DELETE SET NULL,
    id_resumo INT,
    FOREIGN KEY (id_resumo) REFERENCES Resumo(id_resumo) ON DELETE SET NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

CREATE TABLE Mini_jogo (
    id_minigame INT PRIMARY KEY AUTO_INCREMENT,
    tipo_de_jogo VARCHAR(255) NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    conteudo VARCHAR(255),
    dificuldade VARCHAR(255) NOT NULL
);

CREATE TABLE Progressao (
    data_inicio DATETIME NOT NULL,
    id_usuario INT NOT NULL,
    id_artigo INT NOT NULL,
    porcentagem DECIMAL(5,2) ,
    ultima_atualizacao DATETIME NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
CONSTRAINT chk_progresso_valido CHECK (porcentagem BETWEEN 0 AND 100)
);

CREATE TABLE Envia_Arquivos (
    id_envio INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    data_envio DATETIME NOT NULL,
    id_artigo INT,
    id_resumo INT,
    tipo_conteudo VARCHAR(10) NOT NULL,
        CONSTRAINT chk_tipo_conteudo_valido CHECK(
            (tipo_conteudo = 'artigo' AND id_artigo IS NOT NULL AND id_resumo IS NULL) 
            OR
            (tipo_conteudo = 'resumo' AND id_resumo IS NOT NULL AND id_artigo IS NULL)
            ),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_artigo) REFERENCES Artigo(id_artigo) ON DELETE SET NULL,
    FOREIGN KEY (id_resumo) REFERENCES Resumo(id_resumo) ON DELETE SET NULL,
    FOREIGN KEY (id_arquivo) REFERENCES Arquivo(id_arquivo) ON DELETE CASCADE
);

CREATE TABLE Jogo (
  id_jogo INT PRIMARY KEY AUTO_INCREMENT,
  id_minigame INT NOT NULL,
  id_artigo INT NOT NULL,
  FOREIGN KEY (id_minigame) REFERENCES Mini_jogo(id_minigame),
  FOREIGN KEY (id_artigo) REFERENCES Artigo(id_artigo)
);

CREATE INDEX idx_usuario_artigo ON Artigo(id_usuario);
CREATE INDEX idx_usuario_resumo ON Resumo(id_usuario);
CREATE INDEX idx_envia_usuario ON Envia_Arquivos(id_usuario);
CREATE INDEX idx_envia_conteudo_tipo ON Envia_Arquivos(tipo_conteudo);

CREATE INDEX idx_titulo_artigo ON Artigo(titulo);
CREATE INDEX idx_titulo_resumo ON Resumo(titulo);

CREATE TABLE Log_Acoes (
    id_log INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_usuario INT NOT NULL,
    acao VARCHAR(100) NOT NULL,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);