SELECT * FROM departamentos ;

-- 3) Liste todos os funcionários mostrando todos os atributos.

SELECT * FROM funcionarios ;

-- 4) Liste todos os funcionários mostrando nome e salários.

SELECT nome , salario FROM funcionarios ;

-- 5) Selecionar todos os funcionários que ganham igual ou acima de 3000.00.

SELECT nome , salario FROM funcionarios WHERE salario >= 3000.00 ;

-- 6) Selecionar todos os funcionários que são homens e ganham igual ou acima de 3000.

SELECT sexo , salario From funcionarios WHERE sexo = 'M' and salario >= 3000.00 ;

-- 7) Selecionar todos os funcionários do departamento de vendas.





