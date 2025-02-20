CREATE TABLE roles (id SERIAL PRIMARY KEY, name VARCHAR(10) UNIQUE NOT NULL);
CREATE TABLE users (id SERIAL PRIMARY KEY, first_name VARCHAR(20), last_name VARCHAR(20), email VARCHAR(30) UNIQUE NOT NULL, password VARCHAR(20) NOT NULL, role_id INT REFERENCES roles(id));

INSERT INTO roles (name) VALUES
  ("user"),
  ("admin");

INSERT INTO users (first_name, last_name, email, password, role_id) VALUES
    ('Ophir', 'Gal', 'ophirgal2@gmail.com', '12345678', 2),
    ('Jane', 'Smith', 'jane@gmail.com', '123456', 1);