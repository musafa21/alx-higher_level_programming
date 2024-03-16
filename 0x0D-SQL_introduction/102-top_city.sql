-- Display the top 3 cities' temperature during July and August, ordered by temperature in descending order
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 or month = 8
ORDER BY temperature DESC
LIMIT 3;