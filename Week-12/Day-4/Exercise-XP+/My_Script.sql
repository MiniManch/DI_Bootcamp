-- CREATE DATABASE bootcamp;
-- CREATE TABLE students(
-- 	id SERIAL UNIQUE,
--     f_name VARCHAR(50),
--     l_name VARCHAR(50),
--     birth_date DATE -- can also be YEAR or DATETIME
-- );

-- INSERT INTO students(f_name,l_name,birth_date) VALUE ('Marc','Benichou','1998-11-02');
-- INSERT INTO students(f_name,l_name,birth_date) VALUE ('Yoan','Cohen','2010-12-03');
-- INSERT INTO students(f_name,l_name,birth_date) VALUE ('Lea','Benichou','1987-07-27');
-- INSERT INTO students(f_name,l_name,birth_date) VALUE ('Amelia','Dux','1996-04-07');
-- INSERT INTO students(f_name,l_name,birth_date) VALUE ('David','Grez','2006-06-14');
-- INSERT INTO students(f_name,l_name,birth_date) VALUE ('Homer','Simpson','1980-10-03');
-- INSERT INTO students(f_name,l_name,birth_date) VALUE ('Emanuel','Rokah','1996-05-02');

-- Fetch all of the data from the table.
SELECT * FROM students;
-- Fetch all of the students first_names and last_names.
SELECT f_name,l_name FROM students;
-- -- For the following questions, only fetch the first_names and last_names of the students.
-- -- Fetch the student which id is equal to 2.
SELECT f_name,l_name FROM students WHERE id = 2;
-- -- Fetch the student whose last_name is Benichou AND first_name is Marc.
SELECT f_name,l_name FROM students WHERE f_name = 'Marc' AND l_name = 'Benichou';
-- -- Fetch the students whose last_names are Benichou OR first_names are Marc.
SELECT f_name,l_name FROM students WHERE f_name = 'Marc' OR l_name = 'Benichou';
-- -- Fetch the students whose first_names contain the letter a
SELECT f_name,l_name FROM students WHERE f_name LIKE '%a%';
-- -- Fetch the students whose first_names start with the letter a.
SELECT f_name,l_name FROM students WHERE f_name LIKE 'a%';
-- -- Fetch the students whose first_names end with the letter a.
SELECT f_name,l_name FROM students WHERE f_name LIKE '%a';
-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
SELECT f_name,l_name FROM students WHERE SUBSTRING(f_name,-2,1 ) = 'a';
-- Fetch the students whose id’s are equal to 1 AND 3 .
SELECT f_name,l_name FROM students WHERE id = 1 OR id = 3;
-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
SELECT * FROM students WHERE birth_date >= '2000-01-01';
