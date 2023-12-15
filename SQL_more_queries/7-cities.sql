-- create the database 'hbtn_0d_usa' and the table 'cities' inside it
-- cities description:
--  id INT unique, auto-generated, can't be NULL and PK
--  state_id INT, can't be NULL and must be a FK that references to 'id'
--  name VARCHAR(256) can't be NULL
-- if 'hbtn_0d_usa' already exists, the script should not fail
-- id 'cities' already exists, the scriot should not fa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
