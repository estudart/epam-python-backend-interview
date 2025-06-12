"""
Write a query to identify the top 2 Power Users who sent the highest number of 
messages on Microsoft Teams in August 2022. Display the IDs of these 2 users 
along with the total number of messages they sent. Output the results in 
descending order based on the count of the messages.

Assumption:

No two users have sent the same number of messages in August 2022.

SELECT 
  sender_id,
  COUNT(*) as message_count
FROM
  messages
WHERE
  EXTRACT(MONTH FROM sent_date) = '08'
  AND EXTRACT(YEAR FROM sent_date) = '2022'
GROUP BY
  sender_id
ORDER BY
  message_count DESC
LIMIT
  2;
"""

"""
Assume you're given a table containing job postings from various companies on the 
LinkedIn platform. Write a query to retrieve the count of companies that have 
posted duplicate job listings.

Definition:

Duplicate job listings are defined as two job listings within the same company 
that share identical titles and descriptions.

WITH duplicate_companies AS
(
  SELECT 
    company_id
  FROM
    job_listings
  GROUP BY
    company_id,
    title,
    description
  HAVING
    COUNT(company_id) > 1
)  

SELECT
  COUNT(*) AS duplicate_companies
FROM
  duplicate_companies
"""

"""
Companies often perform salary analyses to ensure fair compensation practices. One 
useful analysis is to check if there are any employees earning more than their 
direct managers.

As a HR Analyst, you're asked to identify all employees who earn more than their 
direct managers. The result should include the employee's ID and name.

SELECT 
  emp.employee_id,
  emp.name as employee_name
FROM 
  employee as emp
WHERE
  emp.salary > (
    SELECT
      salary
    FROM 
      employee
    WHERE
      employee_id = emp.manager_id
  )
"""

"""
Given the reviews table, write a query to retrieve the average star rating for each 
product, grouped by month. The output should display the month as a numerical value, 
product ID, and average star rating rounded to two decimal places. Sort the output 
first by month and then by product ID.

SELECT 
  EXTRACT(MONTH FROM submit_date) as mth,
  product_id as product,
  ROUND(AVG(stars), 2) as stars
FROM 
  reviews
GROUP BY
  mth,
  product
"""