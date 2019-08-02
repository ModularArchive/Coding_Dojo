SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;