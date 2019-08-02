SELECT countries.name, languages.language, languages.percentage
FROM countries
	JOIN languages on countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;