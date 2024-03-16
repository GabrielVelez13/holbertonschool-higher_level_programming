-- 
SELECT cities.id, cities.state_id, states.name;
FROM hbtn_0d_usa
GROUP BY cities.id ASC;
