-- Tabela de Alunos
CREATE TABLE Aluno (
    id NUMERIC(10) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    data_nascimento DATE
);

-- Tabela de Autores
CREATE TABLE Autor (
    id NUMERIC(10) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela de Categorias
CREATE TABLE Categoria (
    id NUMERIC(10) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

-- Tabela de Livros
CREATE TABLE Livro (
    id NUMERIC(10) PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    ano_publicacao INT,
    id_categoria NUMERIC(10),
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id) ON DELETE SET NULL
);

-- Tabela de Relacionamento entre Livros e Autores (M:N)
CREATE TABLE Livro_Autor (
    id_livro NUMERIC(10),
    id_autor NUMERIC(10),
    PRIMARY KEY (id_livro, id_autor),
    FOREIGN KEY (id_livro) REFERENCES Livro(id) ON DELETE CASCADE,
    FOREIGN KEY (id_autor) REFERENCES Autor(id) ON DELETE CASCADE
);

-- Tabela de Empréstimos (Relacionamento M:N entre Aluno e Livro)
CREATE TABLE Emprestimo (
    id NUMERIC(10) PRIMARY KEY,
    id_aluno NUMERIC(10),
    id_livro NUMERIC(10),
    data_emprestimo DATE NOT NULL DEFAULT CURRENT_DATE,
    data_devolucao DATE,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id) ON DELETE CASCADE,
    FOREIGN KEY (id_livro) REFERENCES Livro(id) ON DELETE CASCADE
);

-- Inserção de dados
INSERT INTO Aluno (id, nome, email, telefone, data_nascimento) VALUES
(1, 'João Silva', 'joao@email.com', '1111-1111', '2005-04-12'),
(2, 'Maria Oliveira', 'maria@email.com', '2222-2222', '2006-06-23'),
(3, 'Carlos Santos', 'carlos@email.com', '3333-3333', '2004-09-15'),
(4, 'Ana Souza', 'ana@email.com', '4444-4444', '2005-11-30'),
(5, 'Lucas Pereira', 'lucas@email.com', '5555-5555', '2006-01-21'),
(6, 'Mariana Lima', 'mariana@email.com', '6666-6666', '2004-07-19'),
(7, 'Pedro Rocha', 'pedro@email.com', '7777-7777', '2005-02-10'),
(8, 'Fernanda Costa', 'fernanda@email.com', '8888-8888', '2006-12-05'),
(9, 'Ricardo Nunes', 'ricardo@email.com', '9999-9999', '2004-03-08'),
(10, 'Sofia Mendes', 'sofia@email.com', '1010-1010', '2005-08-27');

INSERT INTO Autor (id, nome) VALUES
(1, 'Machado de Assis'),
(2, 'Clarice Lispector'),
(3, 'José de Alencar'),
(4, 'Monteiro Lobato'),
(5, 'Graciliano Ramos');

INSERT INTO Categoria (id, nome) VALUES
(1, 'Romance'),
(2, 'Ficção'),
(3, 'Fantasia'),
(4, 'História'),
(5, 'Aventura');

INSERT INTO Livro (id, titulo, ano_publicacao, id_categoria) VALUES
(1, 'Dom Casmurro', 1899, 1),
(2, 'O Alienista', 1882, 2),
(3, 'Iracema', 1865, 4),
(4, 'Memórias Póstumas de Brás Cubas', 1881, 1),
(5, 'Sítio do Picapau Amarelo', 1921, 3),
(6, 'Vidas Secas', 1938, 1),
(7, 'A Moreninha', 1844, 1),
(8, 'Capitães da Areia', 1937, 5),
(9, 'O Guarani', 1857, 4),
(10, 'O Cortiço', 1890, 2);

INSERT INTO Livro_Autor (id_livro, id_autor) VALUES
(1, 1), (1, 2),
(2, 1), (2, 3),
(3, 3), (3, 4),
(4, 1), (4, 5),
(5, 4), (5, 2),
(6, 5), (6, 1),
(7, 3), (7, 5),
(8, 2), (8, 4),
(9, 3), (9, 1),
(10, 1), (10, 2);

INSERT INTO Emprestimo (id, id_aluno, id_livro, data_emprestimo, data_devolucao) VALUES
(1, 1, 2, '2024-01-01', '2024-01-15'),
(2, 1, 3, '2024-01-16', '2024-02-01'),
(11, 1, 4, '2024-02-05', '2024-02-20'),
(12, 1, 5, '2024-03-10', '2024-03-25'),
(3, 2, 4, '2024-01-05', '2024-01-20'),
(4, 2, 5, '2024-02-10', '2024-02-25'),
(13, 2, 6, '2024-03-15', '2024-04-01'),
(14, 2, 7, '2024-04-05', '2024-04-20'),
(5, 3, 6, '2024-01-12', '2024-01-28'),
(6, 3, 7, '2024-02-15', '2024-03-01'),
(15, 3, 8, '2024-03-20', '2024-04-05'),
(16, 3, 9, '2024-04-10', '2024-04-25'),
(7, 4, 8, '2024-01-18', '2024-02-03'),
(8, 4, 9, '2024-02-22', '2024-03-10'),
(17, 4, 10, '2024-03-15', '2024-04-01'),
(18, 4, 1, '2024-04-05', '2024-04-20'),
(9, 5, 10, '2024-02-01', '2024-02-16'),
(10, 5, 1, '2024-03-05', '2024-03-20'),
(19, 5, 2, '2024-04-01', '2024-04-15'),
(20, 5, 3, '2024-05-01', '2024-05-15');
