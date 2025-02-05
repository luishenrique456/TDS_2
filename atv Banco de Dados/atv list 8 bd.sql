
-- 1. Encontrar o nome e valor de todos os produtos com preço superior a 10.0.

SELECT	nome , preco
FROM	produtos
WHERE	preco > 10;


-- 2.Listar a data de todos os pedidos feitos por um cliente específico, identificado pelo cliente
-- com id = 2.

SELECT	p.data_pedido
FROM	clientes c , pedidos p
WHERE	c.id_cliente = 2 AND
		c.id_cliente = p.id_cliente;



-- SUM, AVG, MIN, MAX, COUNT
-- 3. Listar a quantidade de pedidos realizados pelo cliente com id = 3

SELECT	COUNT(*)
FROM	pedidos pe , clientes c
WHERE	c.id_cliente = 3 AND
		c.id_cliente = pe.id_cliente;





-- 4. Listar o nome, quantidade e preço unitário dos produtos que foram comprados em um
-- pedido específico (id_pedido = 1)


SELECT	pro.nome , pp.quantidade , pp.preco_unitario 
FROM	pedidos_produtos pp , produtos pro
WHERE	pp.id_pedido = 1 AND
		pro.id_produto = pp.id_produto;






-- 5. Listar a quantidade de pedidos realizados pelo cliente com nome = ‘Beltrano’.


SELECT	COUNT(p.id_pedido)
FROM	clientes c , pedidos p
WHERE	c.nome = 'Beltrano' AND
		c.id_cliente = p.id_cliente;





-- 6. Calcular o valor total do pedido com id = 2.


SELECT
FROM
WHERE





-- 7. Calcular o valor total de todos os pedidos do cliente com id = 1.

SELECT
FROM
WHERE




