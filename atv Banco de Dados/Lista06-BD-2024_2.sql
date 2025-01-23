DROP TABLE IF EXISTS funcionarios;

DROP TABLE IF EXISTS departamentos;

CREATE TABLE departamentos (
    numero_departamento NUMERIC(3,0) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE funcionarios (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sexo CHAR(1) CHECK (sexo IN ('M', 'F')),
    salario NUMERIC(10,2),
    numero_departamento NUMERIC(3,0) REFERENCES departamentos(numero_departamento)
);

/* ---------------------------------------------------- */
/* povoando a tabela departamentos */
INSERT INTO departamentos (numero_departamento, nome)
VALUES (101, 'Vendas');

INSERT INTO departamentos (numero_departamento, nome)
VALUES (202, 'Estoque');

INSERT INTO departamentos (numero_departamento, nome)
VALUES (303, 'Contabilidade');

/* ---------------------------------------------------- */
/* povoando a tabela funcionarios do departamento de vendas */
INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('11111111111', 'Ana Costa', 'F', 3000.00, 101);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('11111111112', 'Carlos Souza', 'M', 3200.00, 101);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('11111111113', 'Fernanda Lima', 'F', 3100.00, 101);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('11111111114', 'Gabriel Rocha', 'M', 3300.00, 101);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('11111111115', 'Luiza Martins', 'F', 3400.00, 101);

/* ---------------------------------------------------- */
/* povoando a tabela funcionarios do departamento de Estoque */
INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('22222222221', 'Marcos Silva', 'M', 2500.00, 202);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('22222222222', 'Rafaela Sousa', 'F', 2700.00, 202);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('22222222223', 'Diego Andrade', 'M', 2600.00, 202);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('22222222224', 'Juliana Alves', 'F', 2800.00, 202);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('22222222225', 'Renato Ferreira', 'M', 2900.00, 202);

/* ---------------------------------------------------- */
/* povoando a tabela funcionarios do departamento de Contabilidade */
INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('33333333331', 'Paula Ramos', 'F', 4000.00, 303);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('33333333332', 'Ricardo Mendes', 'M', 4200.00, 303);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('33333333333', 'Cláudia Nunes', 'F', 4100.00, 303);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('33333333334', 'Eduardo Santos', 'M', 4300.00, 303);

INSERT INTO funcionarios (cpf, nome, sexo, salario, numero_departamento) 
VALUES ('33333333335', 'Vanessa Rocha', 'F', 4400.00, 303);

/* ---------------------------------------------------- */


