DROP TABLE users;

CREATE TABLE users(
id  INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
age INTEGER CHECK(age >= 0)
)

INSERT INTO users (name, age) VALUES ("рома", "15")
