/*
CREATE TABLE Equipamentos (
    id_equipamento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    quantidade INT NOT NULL
);
*/

/*
CREATE TABLE Colaboradores (
    id_colaborador INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(15),
    cargo VARCHAR(50)
);
*/

/*
CREATE TABLE Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,  -- Lembre-se de criptografar a senha!
    id_colaborador INT,
    FOREIGN KEY (id_colaborador) REFERENCES Colaboradores(id_colaborador)
);
*/

/*
CREATE TABLE Emprestimos (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
    id_colaborador INT,
    id_equipamento INT,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE,
    status ENUM('pendente', 'concluído', 'atrasado') DEFAULT 'pendente',
    FOREIGN KEY (id_colaborador) REFERENCES Colaboradores(id_colaborador),
    FOREIGN KEY (id_equipamento) REFERENCES Equipamentos(id_equipamento)
);
*/