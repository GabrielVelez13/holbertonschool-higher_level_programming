-- Order the scores from highest to lowest, but only show scores that are 10 or higher.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
