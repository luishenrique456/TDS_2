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
		e.id_aluno = a.id AND
		e.id_livro = l.id ;

-- Questao 03 --
-- Listar o nome do aluno e o titulo do livro para cada emprestimo realizado

SELECT	a.nome , l.titulo 
FROM	livro l , emprestimo e , aluno a
WHERE	e.id_aluno = a.id AND
		e.id_livro = l.id ;




-- Questao 04 --
-- Listar o nome do autor e o titulo de todos os livros que ele escreveu

SELECT	aut.nome , l.titulo
FROM	autor aut , livro l , livro_autor la
WHERE	aut.id = la.id_autor AND
		l.id = la.id_livro ;


-- Questao 05 --
-- Listar a quantidade de emprestimos de livros escritos pelo Machado de Assis

SELECT	COUNT(e.id)
FROM	autor aut , emprestimo e , livro_autor la , livro l
WHERE	aut.nome = 'Machado de Assis' AND
		aut.id = la.id_autor AND
		l.id = la.id_livro AND
		l.id = e.id_livro;
		



		
-- Questao 6
-- Selecionar os nomes dos alunos que já pegaram emprestado o livro "Dom Casmurro".

SELECT	a.nome
FROM	aluno a , emprestimo e , livro l
WHERE	l.titulo = 'Dom Casmurro' AND
		a.id = e.id_aluno AND
		e.id_livro = l.id ;




-- Questao 7
-- Contar quantos livros da categoria "Romance" já foram emprestados.

SELECT	COUNT(e.id)
FROM	categoria ca , livro l , emprestimo e
WHERE	ca.nome = 'Romance' AND
		ca.id = l.id_categoria AND
		l.id = e.id_livro;


-- Questao 8
-- Listar o nome dos alunos que pegaram emprestado livros da categoria "Fantasia".

SELECT	a.nome 
FROM	aluno a , categoria ca , livro l , emprestimo e
WHERE	ca.nome = 'Fantasia' AND
		ca.id = l.id_categoria AND
		l.id = e.id_livro AND
		a.id = e.id_aluno ;




-- Questao 9
-- Selecionar o nome dos autores que escreveram livros da categoria "História".

SELECT	aut.nome 
FROM	autor aut , livro_autor la , livro l , categoria ca
WHERE	ca.nome = 'História' AND
		aut.id = la.id_autor AND
		l.id = la.id_livro AND
		l.id_categoria = ca.id ;




-- Questao 10
-- Contar quantos livros de "Clarice Lispector" já foram emprestados.

SELECT	COUNT(e.id_livro)
FROM	autor aut , livro_autor la , livro l , emprestimo e
WHERE	aut.nome = 'Clarice Lispector' AND
		aut.id = la.id_autor AND
		l.id = la.id_livro AND
		l.id = e.id_livro;



