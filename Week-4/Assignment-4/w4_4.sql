-- Q1: select all articles with their author’s email.
SELECT article, email FROM assignment.article a
LEFT JOIN assignment.user u ON a.user_id = u.id

-- Q2: select articles from 7th to 12th sorted by id.
SELECT id, article FROM (
	SELECT * 
    ,ROW_NUMBER() OVER (ORDER BY ID) row_num
    FROM assignment.article) art
WHERE row_num BETWEEN 7 AND 12