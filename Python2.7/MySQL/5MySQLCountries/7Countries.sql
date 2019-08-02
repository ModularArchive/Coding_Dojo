SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
	JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina'
	AND cities.district = 'Buenos Aires'
    AND cities.population > 500000;