show databases;



use datarepresentation;


create table book (
id int NOT NULL auto_increment,
title varchar(250),
author varchar(250),
price int,
PRIMARY KEY(id)
);

show tables;

select * from book;

select * from student;

insert into student (firstname, age) values ("Mary", 21);

drop database datarepresentation;
