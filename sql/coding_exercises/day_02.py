"""
Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

The CITY table is described as follows:

SELECT *
FROM CITY as ct
WHERE ct.CountryCode = 'USA'
AND ct.POPULATION > 100000;
"""

"""
Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

The CITY table is described as follows:
SELECT CT.NAME
FROM CITY AS CT
WHERE CT.COUNTRYCODE = 'USA'
AND CT.POPULATION > 120000;
"""

"""
Query all columns (attributes) for every row in the CITY table.

The CITY table is described as follows:

SELECT *
FROM CITY;
"""

"""
Query all columns for a city in CITY with the ID 1661.

The CITY table is described as follows:

SELECT *
FROM CITY AS CT
WHERE CT.ID = 1661;
"""

"""
Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

The CITY table is described as follows:

SELECT *
FROM CITY AS CT
WHERE CT.COUNTRYCODE = 'JPN'
"""

"""
Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
The CITY table is described as follows:

SELECT CT.NAME
FROM CITY AS CT
WHERE CT.COUNTRYCODE = 'JPN'
"""

"""
Query a list of CITY and STATE from the STATION table.
The STATION table is described as follows:

SELECT ST.NAME, ST.CITY
FROM STATION AS ST;
"""

"""
Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
The STATION table is described as follows:

SELECT DISTINCT ST.CITY
FROM STATION AS ST
WHERE MOD(ST.ID, 2) = 0;
"""

"""
Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows:

SELECT COUNT(*) AS total_items FROM STATION AS ST

SELECT COUNT(DISTINCT ST.CITY) AS distinct_count FROM STATION AS ST

SELECT
    (SELECT COUNT(*) AS total_items FROM STATION AS ST) - (SELECT COUNT(DISTINCT ST.CITY) AS distinct_count FROM STATION AS ST)
"""

"""
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
The STATION table is described as follows:

SELECT ST.CITY, LENGTH(ST.CITY) AS NAME_LENGTH
FROM STATION AS ST
ORDER BY LENGTH(ST.CITY), ST.CITY
LIMIT 1;

SELECT ST.CITY, LENGTH(ST.CITY) AS NAME_LENGTH
FROM STATION AS ST
ORDER BY LENGTH(ST.CITY) DESC, ST.CITY
LIMIT 1;

"""

"""
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

SELECT DISTINCT ST.CITY
FROM STATION AS ST
WHERE RIGHT(ST.CITY, 1) IN ('A', 'E', 'I', 'O', 'U');
"""

"""
SELECT DISTINCT ST.CITY
FROM STATION AS ST
WHERE RIGHT(ST.CITY, 1) IN ('A', 'E', 'I', 'O', 'U')
AND LEFT(ST.CITY, 1) IN ('A', 'E', 'I', 'O', 'U');
"""