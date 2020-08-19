
/*MYSQL*/

/*a. Insert a new city to include, id: 3, name: Tokyo, Country: Japan, Population: 9,2 million, Hemisphere: North.*/


INSERT INTO City (city_id, city_name, city_country, city_population, city_hemisphere)
       VALUES (3, 'Tokyo', 'Japan', 9200000, 'N');

COMMIT;


/*b. Update Tokyo population to 9,73 million.*/

UPDATE City SET city_population = 9730000 WHERE city_name = 'Tokyo';


/*c. Query the city table for the cities in the northern hemispher and with population greater than 10 million*/

SELECT city_name FROM City WHERE city_hemisphere='N' and city_population > 10000000;



/*d. Query the city table for the sum of the populations of cities in the northern hemisphere.*/

SELECT SUM(city_population) FROM City WHERE city_hemisphere = 'N';


/*e. Query for athletes first name, last name and birth place*/

SELECT athlete_first_name, athlete_last_name, city_name
FROM Athletes
INNER JOIN City ON athlete_birthplace = city_id;


/*f. Query for all athletes who were born in the southern hemisphere*/

SELECT athlete_first_name, athlete_last_name, city_hemisphere
FROM Athletes
INNER JOIN City on athlete_birthplace = city_id
WHERE city_hemisphere = 'S';


/*g. Query for female athletes born in a city with population over 5 million.*/


SELECT athlete_first_name, athlete_last_name, athlete_sex, city_name, city_population
FROM Athletes
INNER JOIN City on athlete_birthplace = city_id
WHERE athlete_sex='F' and city_population>5000000 ;


/*h. Query for the athlete born in a city that has the highestpopulation.*/


SELECT athlete_first_name, athlete_last_name, city_name, city_population
FROM Athletes
INNER JOIN City on athlete_birthplace = city_id
ORDER BY city_population DESC LIMIT 1;



