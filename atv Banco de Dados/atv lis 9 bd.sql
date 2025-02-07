-- Questao 01 --
-- Selecionar a quantidade de emprestimos feitos pelo aluno com id = 2
SELECT	COUNT(e.id)
FROM	emprestimo e
WHERE	e.id_aluno = 2;

-- Questao 02 -- 
-- Selecionar os titulos dos livros que já foram emprestados ao aluno com id = 2
SELECT	l.titulo
FROM	emprestimo e, livro l
WHERE	e.id_aluno = 2 AND
		e.id_livro = l.id;

-- Questao 03 --
-- Listar o nome do aluno e o titulo do livro para cada emprestimo realizado
SELECT	a.nome, l.titulo
FROM	aluno a, emprestimo e, livro l
WHERE	a.id = e.id_aluno AND
		l.id = e.id_livro;

-- Questao 04 --
-- Listar o nome do autor e o titulo de todos os livros que ele escreveu
SELECT	a.nome, l.titulo
FROM	livro l, autor a, livro_autor la
WHERE	l.id = la.id_livro AND
		a.id = la.id_autor;

-- Questao 05 --
-- Listar a quantidade de emprestimos de livros escritos pelo Machado de Assis
SELECT	COUNT(e.id)
FROM	emprestimo e, livro l, livro_autor la, autor a
WHERE	a.nome = 'Machado de Assis'	AND
		la.id_autor = a.id	AND
		la.id_livro = l.id	AND
		l.id = e.id_livro;

