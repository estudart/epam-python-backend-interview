"""
SQL Question 1: Compute Total Monthly Revenue per Product
Imagine you work at EPAM Systems and you are given a task where you have to 
analyze the company's monthly revenue for each product. The company has a sales 
database that logs every single sale transaction. Write a SQL query to calculate 
the total monthly revenue for each product.

-- Create the sales table
CREATE TABLE sales (
    sale_id INT,
    sale_date DATE,
    product_id INT,
    unit_price INT,
    quantity INT
);

-- Insert sample data
INSERT INTO sales (sale_id, sale_date, product_id, unit_price, quantity) VALUES
(10, '2020-06-01', 1, 100, 5),
(20, '2020-06-02', 2, 50, 10),
(30, '2020-06-15', 1, 100, 15),
(40, '2020-07-01', 1, 100, 10),
(50, '2020-07-20', 2, 50, 20);

-- QUERY database
SELECT 
	EXTRACT(MONTH FROM sale_date) AS month,
    product_id,
    SUM(unit_price * quantity) AS total_revenue
FROM 
	sales
GROUP BY
	EXTRACT(MONTH FROM sale_date), product_id
ORDER BY month, product_id;
"""

"""
SQL Question 2: Database Design for Employee Time Tracking
As an analyst in EPAM Systems, you are tasked to design and optimize a database for 
tracking employee working hours. The database should hold information about the employees, 
their daily check-in and check-out times, and their assigned projects. In addition, a 
query should be available to compute the total hours logged by each employee per project per month.

An important consideration while designing this system is the capability to process 
hundreds of check-in and check-out events per day, filter events for specific periods, as well 
as accommodate addition/modification of employee records and project assignments.


"""


"""
SQL Question 6: Calculate the average bug resolution time
In EPAM Systems, a software consulting and product development company, bug resolution is of 
utmost importance. As a staff member of the software testing team, you are asked to write a 
SQL query to find the average time (in days) it takes to resolve bugs.

The database has a table called "bugs" which contains the following columns: 
bug_id (ID of the bug), creation_date (date when the bug was raised), 
resolution_date (date when the bug was resolved), project_id (id of the project the bug belongs to).

-- Create bugs table
CREATE TABLE bugs (
    bug_id INT,
    creation_date DATE,
    resolution_date DATE,
    project_id INT
);

-- Insert data into bugs table
INSERT INTO bugs (bug_id, creation_date, resolution_date, project_id) VALUES
(101, '2022-01-01', '2022-01-03', 1),
(102, '2022-01-05', '2022-01-09', 1),
(103, '2022-02-01', '2022-02-05', 2),
(104, '2022-02-10', '2022-02-15', 2),
(105, '2022-03-01', '2022-03-05', 1);

SELECT
	project_id,
    AVG(resolution_date - creation_date) AS average_resolution_days
FROM
	bugs
GROUP BY
	project_id;
"""

"""
Assume you're given two tables containing data about Facebook Pages and their 
respective likes (as in "Like a Facebook Page").

Write a query to return the IDs of the Facebook pages that have zero likes. 
The output should be sorted in ascending order based on the page IDs.

select distinct
  pg.page_id
from 
  pages pg
full outer join 
  page_likes pl on pg.page_id = pl.page_id
where
  pl.page_id is null
order by pg.page_id desc;
"""

"""
You're provided with two tables: the advertiser table contains information 
about advertisers and their respective payment status, and the daily_pay table 
contains the current payment information for advertisers, and it only 
includes advertisers who have made payments.

Write a query to update the payment status of Facebook advertisers based 
on the information in the daily_pay table. The output should include the 
user ID and their current payment status, sorted by the user id.

The payment status of advertisers can be classified into the following categories:

New: Advertisers who are newly registered and have made their first payment.
Existing: Advertisers who have made payments in the past and have recently 
made a current payment.
Churn: Advertisers who have made payments in the past but have not made any 
recent payment.
Resurrect: Advertisers who have not made a recent payment but may have made a 
previous payment and have made a payment again recently.

Before proceeding with the question, it is important to understand the 
possible transitions in the advertiser's status based on the payment status. 
The following table provides a summary of these transitions:

select
  coalesce(ad.user_id, dp.user_id) as user_id,
  case
    when ad.status is null and dp.paid is not null then 'NEW'
    when ad.status = 'NEW' and dp.paid is not null then 'EXISTING'
    when ad.status = 'NEW' and dp.paid is null then 'CHURN'
    when ad.status = 'EXISTING' and dp.paid is not null then 'EXISTING'
    when ad.status = 'EXISTING' and dp.paid is null then 'CHURN'
    when ad.status = 'CHURN' and dp.paid is not null then 'RESURRECT'
    when ad.status = 'CHURN' and dp.paid is null then 'CHURN'
    when ad.status = 'RESURRECT' and dp.paid is not null then 'EXISTING'
    when ad.status = 'RESURRECT' and dp.paid is null then 'CHURN'
  end as new_status
from 
  advertiser as ad
full outer join 
  daily_pay as dp
on ad.user_id = dp.user_id
order by user_id;
"""

"""
Given a table of Facebook posts, for each user who posted at least twice in 2021, 
write a query to find the number of days between each user’s first post of the 
year and last post of the year in the year 2021. Output the user and number of 
the days between each user's first and last post.

select
  user_id,
  extract (day from (max(post_date) - min(post_date))) as days_between
from 
  posts
where
  extract (year from post_date) = '2021'
group by 
  user_id
having count(post_id)>1;

"""