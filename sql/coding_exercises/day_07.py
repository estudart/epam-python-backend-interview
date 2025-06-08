"""
SELECT DISTINCT ST.CITY
FROM STATION AS ST
WHERE LEFT(ST.CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
"""

"""
SELECT DISTINCT ST.CITY
FROM STATION AS ST
WHERE RIGHT(ST.CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
"""

"""
SELECT DISTINCT ST.CITY
FROM STATION AS ST
WHERE RIGHT(ST.CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U')
OR LEFT(ST.CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
"""

"""
SELECT DISTINCT ST.CITY
FROM STATION AS ST
WHERE RIGHT(ST.CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U')
AND LEFT(ST.CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U');
"""

"""
Query the Name of any student in STUDENTS who scored higher than  Marks. 
Order your output by the last three characters of each name. If two or 
more students both have names ending in the same last three characters 
(i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

SELECT ST.NAME
FROM STUDENTS AS ST
WHERE ST.MARKS > 75
ORDER BY RIGHT(ST.NAME, 3), ST.ID;
"""

"""
Write a query that prints a list of employee names (i.e.: the name attribute) 
from the Employee table in alphabetical order.

SELECT EMP.NAME
FROM EMPLOYEE AS EMP
ORDER BY EMP.NAME;
"""

"""
-- PART 1
SELECT CONCAT(Name, '(', LEFT(Occupation, 1), ')')
FROM OCCUPATIONS
ORDER BY Name;

-- PART 2
SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(*), Occupation;
"""

"""
SELECT EMP.NAME
FROM EMPLOYEE AS EMP
WHERE EMP.SALARY > 2000
AND EMP.MONTHS < 10
ORDER BY EMP.EMPLOYEE_ID;
"""

"""
SELECT COUNT(*)
FROM CITY AS CT
WHERE CT.POPULATION > 100000;
"""

"""
SELECT SUM(CT.POPULATION)
FROM CITY AS CT
WHERE CT.DISTRICT = 'California';
"""

"""
SELECT AVG(CT.POPULATION)
FROM CITY AS CT
WHERE CT.DISTRICT = 'California';
"""

"""
SELECT ROUND(AVG(CT.POPULATION))
FROM CITY AS CT;
"""

"""
SELECT SUM(CT.POPULATION)
FROM CITY AS CT
WHERE CT.COUNTRYCODE = 'JPN';
"""

"""
SELECT MAX(CT.POPULATION) - MIN(CT.POPULATION)
FROM CITY AS CT;
"""

"""
SELECT CEIL(
    AVG(EMP.SALARY) -
    AVG(CAST(REPLACE(EMP.SALARY, '0', '') AS UNSIGNED))
) AS error
FROM EMPLOYEES AS EMP;
"""