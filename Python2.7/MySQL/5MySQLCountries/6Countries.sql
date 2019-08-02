SELECT contries.name, countries.government_form, countries.capital
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy'
	AND countries.life_expectancy > 75
	AND countries.capital > 200;