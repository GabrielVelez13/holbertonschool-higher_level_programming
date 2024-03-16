-- Join the two tables cities and states to list all the cities in the states of California and New York. The result should include the city name and the state name. Sort the result by the city id in ascending order.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;