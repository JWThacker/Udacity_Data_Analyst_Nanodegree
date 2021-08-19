-- Query for average global temperatures by year
SELECT year, avg_temp
FROM global_data

-- Query average temperature in Atlanta (where I was born) by year
SELECT year, city, country, avg_temp
FROM city_data
WHERE city = 'Atlanta' AND country = 'United States'
