show databases;

create database datarep;

use datarep;

show tables;

create table student (
id int NOT NULL auto_increment,
firstname varchar(100),
age int(3),
PRIMARY KEY(id)
);


show tables;

desc student;

INSERT INTO student (firstname, age) values ("joe",56);

select * from student;

-- Update
update student set firstname="mary" where id = 1;

-- Delete
Delete from student where id = 1;

drop database datarep;

create database book;


create table book (
id int NOT NULL auto_increment,
title varchar(100),
author varchar(100),
price int(3),
PRIMARY KEY(id)
);

INSERT INTO book (title, author) values ("hhrhrh", "test");

select * from book;