-- number of score

SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score;