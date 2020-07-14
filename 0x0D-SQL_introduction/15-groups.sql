-- Write a script that computes the score average
-- of all records in the table second_tableof the database
-- hbtn_0c_0 in your MySQL server.
SELECT score, count(score) AS number FROM second_table GROUP BY score;
