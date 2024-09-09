# CRUD_Project

----Lista de Import

pip install mysql-connector-python
pip install fastapi
pip install "fastapi[standard]"

----Criação das tabelas necessarias no MYSQL
--Login padrão de ADMIN: admin
--Senha padrão de ADMIN: root

CREATE DATABASE python_crud;

USE python_crud;

CREATE TABLE crud(
id int(4) AUTO_INCREMENT,
firstname varchar(15),
lastname varchar(30),
email varchar(70),
password varchar(20),
birthday date,
PRIMARY KEY (id)
);

CREATE TABLE admin(
id int(4) AUTO_INCREMENT,
user varchar(10),
password varchar(20),
PRIMARY KEY (id)
);

INSERT INTO admin (user, password) VALUES ("admin", "root");