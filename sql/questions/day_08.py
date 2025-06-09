"""
Whats is the difference between WHERE and HAVING in SQL?

WHERE
- Values BEFORE Grouping
- Individual Rows
- SELECT username, followers FROM instagram_data WHERE followers > 1000;

HAVING
- Values AFTER Grouping
- Aggregated Values from Groups of Rows
- SELECT country FROM instagram_data GROUP BY country HAVING AVG(followers) > 100;

"""

"""
Why would you use the CHECK SQL constraint?

The CHECK constraint is used to specify a condition that the data in a column must meet. 
If a row is inserted or updated and the data in the column doesn't meet the condition 
specified by the CHECK constraint, the operation will sadly fail.

For example, you might use a CHECK constraint to ensure that a column contains only 
positive numbers, or that a date is within a certain range.

For example, if you had a table of EPAM Systems employees, here's an example of how to 
use the CHECK constraint in a CREATE TABLE statement:

CREATE TABLE epam_systems_employees (
  id INT PRIMARY KEY,
  salary INT CHECK (salary > 0),
  hire_date DATE CHECK (hire_date >= '1970-01-01')
);
"""

"""
What is the difference between SQL operators ‘BETWEEN’ and ‘IN’?

While both the BETWEEN and IN operators are used to filter data based on some criteria, 
BETWEEN selects for values within a given range, whereas for IN it checks if the value is in a 
given list of values.

For example, say you had a table called epam_systems_employees, which had the salary of the 
employee, along with the country in which they reside.

To find all employees who made between 80kand80kand120k, you could use the BETWEEN operator:
SELECT * 
FROM epam_systems_employees 
WHERE salary BETWEEN 80000 AND 120000;

To find all employees that reside in the US or Canada, you could use the IN operator:
SELECT * 
FROM epam_systems_employees 
WHERE country IN ("USA", "Canada");
"""