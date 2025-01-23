-- 1. Listar todos os alunos com seus respectivos ids, nomes e datas de nascimento.

SELECT * FROM Aluno ;

-- 2. Exibir o nome e a carga horária das disciplinas com carga horária superior a 50 horas.
SELECT nome,carga_horaria 
FROM Disciplina
WHERE carga_horaria > 50 ;

-- 3. Mostrar as disciplinas nas quais o aluno com ID 10 está matriculado.

SELECT * FROM Disciplina ;
