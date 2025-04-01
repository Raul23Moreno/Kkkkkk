CREATE DATABASE IF NOT EXISTS usuarios;
USE usuarios;
CREATE TABLE IF NOT EXISTS usuarios (
    nombre VARCHAR(255) NOT NULL,
    contrasena VARCHAR(255) NOT NULL
);
INSERT INTO usuarios (nombre, contrasena) VALUES ('ramorenoadmin', 'ramoreno23');
