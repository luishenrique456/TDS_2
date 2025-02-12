-- QUESTÃO 01
-- Exibir todas as disciplinas com suas respectivas cargas horarias
SELECT nome, carga_horaria
FROM disciplina;

-- QUESTÃO 02
-- Exibir o nome das disciplinas com a carga horária inferior a 60 horas
SELECT	nome , carga_horaria
FROM	disciplina
WHERE	carga_horaria < 60;

-- QUESTÃO 03
-- Exibir todos os alunos matriculados na disciplina 'Matemática' ordenado por nome.
SELECT a.nome 
FROM aluno a, matricula m , disciplina d
WHERE d.nome = 'Matemática' AND 
		m.aluno_id = a.aluno_id AND
		m.disciplina_id = d.disciplina_id
		ORDER BY a.nome;
		
-- QUESTÃO 04
-- Exibir a quantidade de faltas do aluno de id 16 na disciplina 'Ciências'
SELECT	a.nome, m.faltas
FROM	aluno a, matricula m , disciplina d
WHERE	a.aluno_id = 16 AND
		d.nome = 'Ciências' AND
		a.aluno_id = m.aluno_id AND
		m.disciplina_id = d.disciplina_id;

-- QUESTÃO 05
-- Exibir todos os alunos com a média menor ou igual a 8 na disciplina "História"
SELECT	a.nome
FROM	aluno a , matricula m , disciplina d
WHERE	m.media <= 8 AND
		d.nome = 'História' AND
		a.aluno_id = m.aluno_id AND
		m.disciplina_id = d.disciplina_id;

