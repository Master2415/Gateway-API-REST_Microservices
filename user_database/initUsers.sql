CREATE DATABASE users_db;

\c users_db;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Insertar datos de prueba en la tabla users
INSERT INTO users (name, password, email) VALUES 
('Juan', 'perro', 'juan@email.com'),
('Pedro', 'gato', 'pedro@email.com'),
('Luis', 'casa', 'luis@email.com'),
('Diego', 'sol', 'diego@email.com'),
('Carlos', 'playa', 'carlos@email.com'),
('Sofía', 'luna', 'sofia@email.com'),
('Ana', 'mar', 'ana@email.com'),
('María', 'montaña', 'maria@email.com'),
('Lucía', 'agua', 'lucia@email.com'),
('Miguel', 'aire', 'miguel@email.com'),
('Andrés', 'fuego', 'andres@email.com');


-- psql -U admin -d users_db -f init.sql