CREATE TABLE cookies(
    key character(36) PRIMARY KEY, 
    value character(36) NOT NULL
);

CREATE TABLE users(
    id serial PRIMARY KEY, 
    username character(70) NOT NULL,
    name character(70) NOT NULL,
    sexo character(30) NOT NULL,
    edad integer NOT NULL, 
    password character(20) NOT NULL,
    fecha character (30) NOT NULL
);

INSERT INTO users (username, name, sexo, edad, password, fecha) 
  VALUES ('pedro','Pedro Konstantinoff', 'Masculino', 36,'123', '2008/12/31');

INSERT INTO users (username, name, sexo, edad, password, fecha)
  VALUES ('Usuario 2','Usuario 2', 'Masculino', 36,'pass', '2008/12/31');

INSERT INTO users (username, name, sexo, edad, password, fecha)
  VALUES ('Usuario 4','Usuario 4', 'Masculino', 34,'pass', '2008/12/31');

INSERT INTO users (username, name, sexo, edad, password, fecha)
  VALUES ('Usuario 5','Usuario 5', 'Masculino', 33,'pass', '2008/12/31');

INSERT INTO users (username, name, sexo, edad, password, fecha)
  VALUES ('Usuario 6','Usuario 6', 'Masculino', 38,'pass', '2008/12/31');

INSERT INTO users (username, name, sexo, edad, password, fecha)
  VALUES ('Usuario 7','Usuario 7', 'Masculino', 32,'pass', '2008/12/31');


INSERT INTO cookies (key, value) 
  VALUES ('pedro','123');

SELECT * FROM users;