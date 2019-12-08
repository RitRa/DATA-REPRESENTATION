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

update book set title= "AAA", author="AAA", price=222 where id = 1;

INSERT into book (title, author, price) values ("harry potter", "jk", 12);
INSERT into book (title, author, price) values ("harry potter 2", "jk", 12);

select * from student;

insert into student (firstname, age) values ("Mary", 21);

drop database datarepresentation;
