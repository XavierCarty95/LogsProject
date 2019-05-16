My first Udacity project was to query the results from database that was already provided by Udacity. 

using the psycopg2 module to connect to the database. Used PostgreSQL database for a fictional News. 
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors

Good coding practices
SQL style
Each one of these questions can be answered with a single database query. Your code should get the database to do the heavy lifting by using joins, aggregations, and the where clause to extract just the information you need, doing minimal "post-processing" in the Python code itself.

CREATE VIEW article_authors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;

CREATE VIEW article_views AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;
Views for Question 3

CREATE VIEW logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as LogCount
FROM log
GROUP BY Date;
CREATE VIEW errorlogs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErrorCount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;
