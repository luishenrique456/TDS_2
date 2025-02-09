-- Questao 01 --
-- Selecionar a quantidade de emprestimos feitos pelo aluno com id = 2
SELECT	COUNT(id_aluno)
FROM	emprestimo
WHERE	id_aluno = 2;

-- Questao 02 -- 
-- Selecionar os titulos dos livros que já foram emprestados ao aluno com id = 2

SELECT	l.titulo 
FROM	livro l , emprestimo e , aluno a
WHERE	a.id = 2 AND
		a.id = e.id_aluno AND
		l.id = e.id_livro;



-- Questao 03 --
-- Listar o nome do aluno e o titulo do livro para cada emprestimo realizado

SELECT	a.nome , l.titulo
FROM	livro l , emprestimo e , aluno a
WHERE	l.id = e.id_livro AND
		a.id = e.id_aluno;


-- Questao 04 --
-- Listar o nome do autor e o titulo de todos os livros que ele escreveu

SELECT	aut.nome , l.titulo
FROM	autor aut , livro_autor la , livro l 
WHERE	aut.id = la.id_autor AND
		l.id = la.id_livro ;

-- Questao 05 --
-- Listar a quantidade de emprestimos de livros escritos pelo Machado de Assis

SELECT	COUNT(e.id_livro)
FROM	autor aut , livro_autor la , livro l , emprestimo e
WHERE	aut.nome = 'Machado de Assis' AND
		aut.id = la.id_autor AND
		l.id = la.id_livro AND
		l.id = e.id_livro;



		
-- Questao 6
-- Selecionar os nomes dos alunos que já pegaram emprestado o livro "Dom Casmurro".

SELECT	a.nome 
FROM	livro l , emprestimo e ,aluno a
WHERE	l.titulo = 'Dom Casmurro' AND
		l.id = e.id_livro AND
		a.id = e.id_aluno ;



-- Questao 7
-- Contar quantos livros da categoria "Romance" já foram emprestados.

SELECT	COUNT(e.id_livro)
FROM	categoria ca , livro l , emprestimo e
WHERE	ca.nome = 'Romance' AND
		ca.id = l.id_categoria AND
		l.id = e.id_livro;




-- Questao 8
-- Listar o nome dos alunos que pegaram emprestado livros da categoria "Fantasia".

SELECT	a.nome 
FROM	categoria ca , livro l , emprestimo e , aluno a
WHERE	ca.nome = 'Fantasia' AND
		ca.id = l.id_categoria AND
		l.id = e.id_livro AND
		a.id = e.id_aluno;



-- Questao 9
-- Selecionar o nome dos autores que escreveram livros da categoria "História".

SELECT	aut.nome 
FROM	autor aut , livro_autor la , livro l , categoria ca
WHERE	ca.nome = 'História' AND
		aut.id = la.id_autor AND
		l.id = la.id_livro AND
		l.id_categoria = ca.id;



-- Questao 10
-- Contar quantos livros de "Clarice Lispector" já foram emprestados.

SELECT	COUNT(e.id_livro)
FROM	autor aut , livro_autor la , livro l , emprestimo e
WHERE	aut.nome = 'Clarice Lispector' AND
		aut.id = la.id_autor AND
		l.id = la.id_livro AND
		l.id = e.id_livro;



-- Selecionar nomes dos alunos , data de emprestimo , titulo do livro , nomes da categoria
-- id do livro , nomes do autores

SELECT	a.nome , e.data_emprestimo , l.titulo , ca.nome , la.id_livro , aut.nome
FROM	autor aut , livro_autor la , livro l , categoria ca , emprestimo e , aluno a
WHERE	aut.id = la.id_autor AND
		l.id = la.id_livro AND
		l.id_categoria = ca.id AND
		l.id = e.id_livro AND
		a.id = e.id_aluno ;






