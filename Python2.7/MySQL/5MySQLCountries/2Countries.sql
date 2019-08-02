SELECT countries.name, COUNT(cities.id) as num_cities
FROM countries
	JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY num_cities DESC;