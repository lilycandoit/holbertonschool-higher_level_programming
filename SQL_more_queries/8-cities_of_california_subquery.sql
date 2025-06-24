-- cities of California

USE hbtn_0d_usa;

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM cities WHERE name = 'California'
)
ORDER BY id;