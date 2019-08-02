SELECT countries.region, COUNT(countries.id) AS num_countries
FROM countries
GROUP BY countriesregion
ORDER BY num_countries DESC;