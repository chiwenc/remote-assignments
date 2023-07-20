-- Q1: select all articles with their author’s email.
SELECT article, email FROM assignment.article a
LEFT JOIN assignment.user u ON a.user_id = u.id

-- Q2: select articles from 7th to 12th sorted by id.
SELECT id, article FROM assignment.article
WHERE id BETWEEN 7 AND 12
ORDER BY id