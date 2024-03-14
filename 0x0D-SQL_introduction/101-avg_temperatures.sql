-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending) :-
SELECT city, AVG(temperature * 9/5 + 32) AS avg_temp_fahrenheit
FROM weather_data
GROUP BY city
ORDER BY avg_temp_fahrenheit DESC;
