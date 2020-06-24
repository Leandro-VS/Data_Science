-- drop table INSTRUCTOR
create table INSTRUCTOR(
	ins_id int  NOT NULL,
	lastname varchar(30) NOT NULL,
	firstname varchar(30) NOT NULL,
	city varchar(10),
	country char(2),
	PRIMARY KEY (ins_id)
	)

INSERT INTO INSTRUCTOR
(ins_id, lastname, firstname, city, country)
VALUES
('1', 'Ahuja', 'Rav', 'Toronto', 'CA')

insert into INSTRUCTOR
(ins_id, lastname, firstname, city, country)
values
('2', 'Chong', 'Raul', 'Toronto', 'CA'),
('3', 'Vasudevan', 'Hima', 'Chicago', 'US')

select * from instructor

update INSTRUCTOR
	set city = 'Toronto'
	where ins_id = '1'
	
select * from instructor

select firstname, lastname, country from INSTRUCTOR
	where city= 'Toronto'
	
update INSTRUCTOR
	set city = 'Markham'
	where ins_id = '1'
	
select * from instructor

delete from INSTRUCTOR
	where ins_id = '2'

select * from instructor
	
	
	