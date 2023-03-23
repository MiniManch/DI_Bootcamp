USE miniproject;
-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- );

-- CREATE TABLE SecondTab (
--     id integer 
-- );

-- INSERT INTO FirstTab(id,name) VALUES
-- 	(5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')
-- ;

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)
-- ;

SELECT * FROM SecondTab;
SELECT * FROM FirstTab;

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );

-- I dont understand this one

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
--  you count how many ids are not 5 in the first tab, NULL doesnt count apparently

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab);
    -- will count all the ids from firstab where id is not in the secondtab
	-- I receive 0. i DONT GET THIS since, SELECT ID FROM SECONDTAB gets you all the ids, and there are a tons of ids 
    -- in firsttab that arent in second tab, so IDK
    
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
-- assuming it will count how many ids from firstab are not in secondtab and are not NULL, also NULL from firstab wont be counted