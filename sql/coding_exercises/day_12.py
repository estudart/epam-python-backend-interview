"""
On an online recruiting platform, each recruiting company can make a request for their 
candidates to complete a personalized skill assessment. The assessment can contain tasks in 3 
categories: SQL, Algo, Bug fixing. Following the assessment, the company receives a report 
containing for for each candidate

Their declared years of experience (an integer between 0 to 100) and their score in each 
category. The score is the number of points from 0 to 100 or Null which means there was no 
task in this category.

You’re given a table, assessments with following structure:

-- INIT database
CREATE TABLE assessments (
  id INTEGER NOT NULL,
  experience INTEGER NOT NULL,
  sql INTEGER,
  algo INTEGER,
  bug_fixing INTEGER,
  UNIQUE(id)
);

INSERT INTO assessments (id, experience, sql, algo, bug_fixing) VALUES
(1, 5, 100, NULL, 100),
(2, 10, 100, 100, NULL),
(3, 5, NULL, 100, 100),
(4, 20, NULL, NULL, NULL);

-- QUERY database
WITH scores AS (
  SELECT
    experience,
    (CASE WHEN sql = 100 or sql IS NULL THEN 1 ELSE 0 END +
     CASE WHEN algo = 100 or algo IS NULL THEN 1 ELSE 0 END +
     CASE WHEN bug_fixing = 100 or bug_fixing IS NULL THEN 1 ELSE 0 END) AS max,
  	COUNT(*)
  FROM
  	assessments
  GROUP BY
    experience,
    max
)

SELECT * FROM scores WHERE max = 3;
	
"""