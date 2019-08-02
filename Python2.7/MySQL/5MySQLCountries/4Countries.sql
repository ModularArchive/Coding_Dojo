SELECT countries.name, languages.language, languages.country_id
FROM countries
	JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;