-- Lists all the scores and names from the second_table table, ordered by score in descending order, but only for those records where the name is not null.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;