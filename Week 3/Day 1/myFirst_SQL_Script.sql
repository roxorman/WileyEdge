use wileydataanalysis;
create table students (student_id int, username  varchar(40));
INSERT INTO students (student_id, username) VALUES (1, 'Marco');
INSERT INTO students (student_id, username) VALUES (2, 'Dan');

select * from students;
update students set student_id =2 where username = 'Dan';

alter table students
rename column student_id to id,
rename column username to user;

select * from students;

delete from students where id = 1;
truncate students;

drop table students;

insert into students values(1,"Marco");
insert into students values(2,"dan");
insert into students values(3,"tia");
insert into students values(4,"csilla");
insert into students values(5,"mac");
insert into students values(6,"tamas");
insert into students values(7,"levente");

create table university(uni_name varchar(300), year_founded varchar(300), address varchar (1000));

create table university_new (uni_id int primary key, uni_name varchar(300), year_founded varchar(300), address varchar(1000));
insert into university_new values(1, 'Rhodes', '1904', '124 alps drive');
drop table university;
drop table university_new ;

describe university_new;
select * from student2;


create table student2(id int primary key, user varchar(300) not null, gender char(1) character set ascii,
HANDICAPPED char(1) character set ascii);

insert into student2 values(2, 'jinesh', 'M', 'N');
insert into student2 (id, user, gender, HANDICAPPED) values(3,"Marcos",'M','N');

#######################################################day 2##################################################
select table_name , engine from information_schema.tables where table_name = 'student2';

# MyISAM :- table is having very heavy load or high number of records;

alter table student2 engine ="MyISAM";

repair table student2;

select * from student2;

show table status;

create table vehicle(vehicle_no int primary key auto_increment, model_name varchar(45), price decimal(10,2), selling_price decimal(10,2));

insert into vehicle(model_name, price, selling_price) values('tesla',  '65000', '78000');
insert into vehicle(model_name, price, selling_price) values('suzuki',  '15000', '22000');


select * from vehicle;

create view mercedescar as
select * from vehicle where model_name like '%mercedes%';  #like is used in case mercedes has capitals 
# view:- row level security. Hide complex thing behind view

select * from mercedescar;

lock table vehicle write;
insert into vehicle(model_name, price, selling_price) values('suzuki',  '15000', '22000');
unlock tables;

alter table vehicle add column description varchar(200) not null after vehicle_no;
alter table vehicle add column vehicle_lr_no varchar(200) not null first ;

select * from vehicle;

alter table vehicle add column desc1 varchar(200) default 'This is an existing car' not null first;

show columns from vehicle like '%d%';

show full columns from vehicle;

alter table vehicle change column desc1 descrip varchar(600) after price;

select * from vehicle where model_name = 'suzuki' and selling_price > 20000;

update vehicle set selling_price = 18000 where vehicle_no ='4';

select * from vehicle where vehicle_no in (2,3,4);


create table table1(num_value int);
insert into table1(num_value) values(10),(20),(25);
create table table2(num_value int);
insert into table2(num_value) values(11),(14),(26);

select num_value from table1 where num_value > ANY (select num_value from table2);