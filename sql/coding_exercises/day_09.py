"""
Assume you're given a table Twitter tweet data, write a query to obtain a 
histogram of tweets posted per user in 2022. Output the tweet count per 
user as the bucket and the number of Twitter users who fall into that bucket.

In other words, group the users by the number of tweets they posted in 2022 
and count the number of users in each group.

select
  COUNT(*) as tweet_bucket,
  ct.users_num
from
  (
    select
      tt.user_id as tweet_bucket,
      COUNT(*) as users_num
    from 
      tweets as tt
    where
      extract(year from tweet_date) = '2022'
    group by 
      tt.user_id
  ) as ct
group by
  ct.users_num
order by
  tweet_bucket
"""

"""
Given a table of candidates and their skills, you're tasked with finding the 
candidates best suited for an open Data Science job. You want to find candidates 
who are proficient in Python, Tableau, and PostgreSQL.

Write a query to list the candidates who possess all of the required skills for 
the job. Sort the output by candidate ID in ascending order.

SELECT
  candidates_skills.candidate_id
FROM
  (
    SELECT
      candidate_id,
      STRING_AGG(skill, ',') as skills
    FROM
      candidates
    GROUP BY
      candidate_id
  ) as candidates_skills
WHERE
  candidates_skills.skills LIKE '%Python%'
  AND candidates_skills.skills LIKE '%Tableau%'
  AND candidates_skills.skills LIKE '%PostgreSQL%'
"""

"""
Tesla is investigating production bottlenecks and they need your 
help to extract the relevant data. Write a query to determine which 
parts have begun the assembly process but are not yet finished.

Assumptions:

parts_assembly table contains all parts currently in production, 
each at varying stages of the assembly process. An unfinished part 
is one that lacks a finish_date.

This question is straightforward, so let's approach it with simplicity 
in both thinking and solution.

Effective April 11th 2023, the problem statement and assumptions were 
updated to enhance clarity.

SELECT
  part,
  assembly_step 
FROM 
  parts_assembly
WHERE
  finish_date is NULL;
"""

"""
This is the same question as problem #3 in the SQL Chapter of Ace the Data 
Science Interview!

Assume you're given the table on user viewership categorised by device type 
where the three types are laptop, tablet, and phone.

Write a query that calculates the total viewership for laptops and mobile 
devices where mobile is defined as the sum of tablet and phone viewership. 
Output the total viewership for laptops as laptop_reviews and the total 
viewership for mobile devices as mobile_views.

Effective 15 April 2023, the solution has been updated with a more concise 
and easy-to-understand approach.


SELECT
  (
    SELECT
      COUNT(*)
    FROM
      viewership as vp
    WHERE
      vp.device_type IN ('laptop')
  ) as laptop_views,
  (
    SELECT
      COUNT(*)
    FROM
      viewership as vp
    WHERE
      vp.device_type IN ('tablet', 'phone')
  ) as mobile_views
"""

"""
Imagine you're an HR analyst at a tech company tasked with analyzing employee 
salaries. Your manager is keen on understanding the pay distribution and asks 
you to determine the second highest salary among all employees.

It's possible that multiple employees may share the same second highest salary. 
In case of duplicate, display the salary only once.

SELECT salary  
FROM employee  
WHERE salary = (  
    SELECT MAX(salary)  
    FROM employee  
    WHERE salary < (SELECT MAX(salary) FROM employee)  
);
"""

"""
This is the same question as problem #10 in the SQL Chapter of Ace the Data Science
 Interview!

Given a table of tweet data over a specified time period, calculate the 3-day 
rolling average of tweets for each user. Output the user ID, tweet date, and 
rolling averages rounded to 2 decimal places.

Notes:

A rolling average, also known as a moving average or running mean is a time-series 
technique that examines trends in data over a specified period of time.
In this case, we want to determine how the tweet count for each user changes over 
a 3-day period.
Effective April 7th, 2023, the problem statement, solution and hints for this 
question have been revised.

SELECT    
  user_id,    
  tweet_date,   
  ROUND(AVG(tweet_count) OVER (
    PARTITION BY user_id     
    ORDER BY tweet_date     
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
  ,2) AS rolling_avg_3d
FROM tweets;
"""

"""
Assume you're given tables with information on Snapchat users, including their ages 
and time spent sending and opening snaps.

Write a query to obtain a breakdown of the time spent sending vs. opening snaps as 
a percentage of total time spent on these activities grouped by age group. Round the 
percentage to 2 decimal places in the output.

Calculate the following percentages:
time spent sending / (Time spent sending + Time spent opening)
Time spent opening / (Time spent sending + Time spent opening)
To avoid integer division in percentages, multiply by 100.0 and not 100.
Effective April 15th, 2023, the solution has been updated and optimised.

WITH snaps_statistics AS (
  SELECT
    age.age_bucket,
    SUM(CASE WHEN activities.activity_type = 'send' THEN activities.time_spent ELSE 0 END) as send_timespent,
    SUM(CASE WHEN activities.activity_type = 'open' THEN activities.time_spent ELSE 0 END) as open_timespent,
    SUM(activities.time_spent) AS total_timespent
  FROM 
    activities
  INNER JOIN
    age_breakdown as age
    ON activities.user_id = age.user_id
  WHERE
    activities.activity_type IN ('open', 'send')
  GROUP BY
    age.age_bucket
)

SELECT
  age_bucket,
  ROUND(100.0 * send_timespent/total_timespent, 2) AS send_perc,
  ROUND(100.0 * open_timespent/total_timespent, 2) AS open_perc
FROM
  snaps_statistics;
"""