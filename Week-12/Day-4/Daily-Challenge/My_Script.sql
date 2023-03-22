-- USE actors;
-- CREATE TABLE actors_2(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age INTEGER(2) NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- );
-- INSERT INTO actors_2(
-- first_name ,last_name,age,number_oscars
-- ) VALUES ('Robert','De Niro',80,2);

-- INSERT INTO actors_2(
-- first_name ,last_name,age,number_oscars
-- ) VALUES ('Marlon','Brando',80,2);

-- INSERT INTO actors_2(
-- first_name ,last_name,age,number_oscars
-- ) VALUES ('Denzel','Washington',69,2);

-- INSERT INTO actors_2(
-- first_name ,last_name,age,number_oscars
-- ) VALUES ('Katharine','Hepburn',96,4);

-- INSERT INTO actors_2(
-- first_name ,last_name,age,number_oscars
-- ) VALUES ('Robert','De Niro',80,2);

-- INSERT INTO actors_2(
-- first_name ,last_name,age,number_oscars
-- ) VALUES ('Humphrey','Bogart',58,1);

-- INSERT INTO actors_2(
-- first_name ,last_name,age,number_oscars
-- ) VALUES ('Meryl','Streep',74,3);

-- INSERT INTO actors_2(
-- first_name ,last_name,age,number_oscars
-- ) VALUES ('Daniel','Day-Lewis',66,3);

-- Count how many actors are in the table
SELECT COUNT(*) FROM actors_2;

-- Try to add a new actor with some blank fields. What do you think the outcome will be ?
-- I expect an error because NULL is not the type of data that we specified for each of the columns
-- INSERT INTO actors_2(
-- first_name ,last_name,age,number_oscars
-- ) VALUES (NULL,NULL,NULL,NULL);
