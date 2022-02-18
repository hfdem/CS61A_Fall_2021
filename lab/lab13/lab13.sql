.read data.sql


CREATE TABLE bluedog AS
SELECT  color
       ,pet
FROM students
WHERE color = "blue"
AND pet = "dog";


CREATE TABLE bluedog_songs AS
SELECT  color
       ,pet
       ,song
FROM students
WHERE color = "blue"
AND pet = "dog";


CREATE TABLE smallest_int_having AS
SELECT  time
       ,smallest
FROM students
GROUP BY  smallest
HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
SELECT  first.pet
       ,first.song
       ,first.color
       ,second.color
FROM students AS first , students AS second
WHERE first.time < second.time
AND first.pet = second.pet
AND first.song = second.song;


CREATE TABLE sevens AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE avg_difference AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

