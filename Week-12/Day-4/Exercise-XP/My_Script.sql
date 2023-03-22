-- CREATE DATABASE public;
-- USE public;
-- CREATE TABLE items(
-- 	name VARCHAR(50),
-- 	price INTEGER
-- );

-- CREATE TABLE customers(
-- 	f_name VARCHAR(50),
--     l_name VARCHAR(50)
-- );

-- INSERT INTO items(name, price) VALUES('Small Desk',100);
-- INSERT INTO items(name, price) VALUES('Large Desk',300);
-- INSERT INTO items(name, price) VALUES('Fan',80);

-- INSERT INTO customers(f_name,l_name) VALUES('Greg','Jones');
-- INSERT INTO customers(f_name,l_name) VALUES('Sandra','Jones');
-- INSERT INTO customers(f_name,l_name) VALUES('Scott','Scott');
-- INSERT INTO customers(f_name,l_name) VALUES('Trevor','Green');
-- INSERT INTO customers(f_name,l_name) VALUES('Melanie','Johnson');
 
--  Use SQL to fetch the following data from the database:
-- All the items.
-- SELECT * FROM items;
-- All the items with a price above 80 (80 not included).
-- SELECT * FROM items WHERE price > 80;
-- -- All the items with a price below 300. (300 included)
-- SELECT * FROM items WHERE price < 300;
-- -- All customers whose last name is ‘Smith’ (What will be your outcome?).Nothing, theres no customer like that
-- SELECT * FROM customers WHERE l_name = 'Smith';
-- All customers whose last name is ‘Jones’.
-- SELECT * FROM customers WHERE l_name = 'Jones';
-- -- All customers whose firstname is not ‘Scott’.
-- SELECT * FROM customers WHERE f_name = 'Smith';

