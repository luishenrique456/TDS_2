-- Criando a tabela clientes
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente NUMERIC(10,0) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(15) NULL
);

-- Criando a tabela produtos
CREATE TABLE IF NOT EXISTS produtos (
    id_produto NUMERIC(10,0) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL
);

-- Criando a tabela pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido NUMERIC(10,0) PRIMARY KEY,
    id_cliente NUMERIC(10,0) NOT NULL,
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Criando a tabela associativa pedidos_produtos para relação muitos para muitos
CREATE TABLE IF NOT EXISTS pedidos_produtos (
    id_pedido NUMERIC(10,0) NOT NULL,
    id_produto NUMERIC(10,0) NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_pedido, id_produto),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- Povoamento da tabela clientes
INSERT INTO clientes (id_cliente, nome, email, telefone) VALUES
(1, 'Fulano', 'fulano@email.com', '11111111111'),
(2, 'Beltrano', 'beltrano@email.com', '22222222222'),
(3, 'Ciclano', 'ciclano@email.com', '33333333333'),
(4, 'Silva', 'silva@email.com', '44444444444'),
(5, 'Santos', 'santos@email.com', '55555555555')
ON CONFLICT (id_cliente) DO NOTHING;

-- Povoamento da tabela produtos
INSERT INTO produtos (id_produto, nome, preco, estoque) VALUES
(1, 'Refrigerante', 10.00, 100),
(2, 'Café', 15.50, 100),
(3, 'Molho de Tomate', 8.75, 100),
(4, 'Macarrão', 20.00, 100),
(5, 'Feijão', 5.50, 100),
(6, 'Arroz', 12.25, 100),
(7, 'Açúcar', 9.99, 100),
(8, 'Sal', 18.40, 100),
(9, 'Óleo de Soja', 25.00, 100),
(10, 'Manteiga', 30.00, 100),
(11, 'Leite', 7.30, 100),
(12, 'Queijo', 14.20, 100),
(13, 'Presunto', 22.50, 100),
(14, 'Pão', 19.99, 100),
(15, 'Biscoito', 27.75, 100),
(16, 'Chocolate', 6.80, 100),
(17, 'Farinha de Trigo', 11.50, 100),
(18, 'Maionese', 16.30, 100),
(19, 'Ketchup', 13.00, 100),
(20, 'Mostarda', 9.50, 100)
ON CONFLICT (id_produto) DO NOTHING;

-- Povoamento da tabela pedidos e pedidos_produtos
CREATE SEQUENCE pedidos_id_pedido_seq;

DO $$
DECLARE i NUMERIC(10,0);
DECLARE j NUMERIC(10,0);
DECLARE pedido_id NUMERIC(10,0);
DECLARE produto_id NUMERIC(10,0);
DECLARE quantidade INT;
BEGIN
    FOR i IN 1..5 LOOP  -- Para cada cliente
        FOR j IN 1..3 LOOP  -- Criando 3 pedidos por cliente
            INSERT INTO pedidos (id_pedido, id_cliente) VALUES (NEXTVAL('pedidos_id_pedido_seq'), i) RETURNING id_pedido INTO pedido_id;
            FOR produto_id IN 1..5 LOOP  -- Adicionando 5 produtos por pedido
                quantidade := floor(random() * 10 + 1); -- Quantidade aleatória entre 1 e 10
                INSERT INTO pedidos_produtos (id_pedido, id_produto, quantidade, preco_unitario)
                VALUES (pedido_id, produto_id, quantidade, 
                        (SELECT preco FROM produtos WHERE id_produto = produto_id));
            END LOOP;
        END LOOP;
    END LOOP;
END $$;


