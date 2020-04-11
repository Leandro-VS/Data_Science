-- Query 1
select  * from Employees;
select F_NAME, address from Employees
	where Address like '%Elgin,IL';
	
-- Query 2 
select F_name, B_date from Employees
	where B_DATE like  '197%' ;

-- Query 3
select F_name, salary from Employees
	where Dep_ID = 5 and (salary between 60000 and 70000);
	
-- Query 4A
select F_name,  Dep_ID from Employees
	order by Dep_ID;

-- Query 4B
select F_NAME, L_NAME, DEP_ID from Employees
	order by Dep_ID desc, L_name desc;
	
-- Query 5A
select Dep_ID, count(Dep_ID)
	as count from Employees group by Dep_ID;
	
-- Query 5B
select Dep_ID, count(*), avg(Salary) from Employees 
	group by Dep_ID;

-- Query 5C
select Dep_ID, count(*) as NUM_EMPLOYEES, avg(Salary) as AVG_SALARY
	from Employees 
	group by Dep_ID;
	
-- Query 5D
select Dep_ID, count(*) as NUM_EMPLOYEES, avg(Salary) as AVG_SALARY
	from Employees 
	group by Dep_ID
	order by AVG_salary;
	
-- Query 5E
select Dep_ID, count(*) as NUM_EMPLOYEES, avg(Salary) as AVG_SALARY
	from Employees 
	group by Dep_ID
	having count(*) < 4
	order by AVG_salary;
	
-- Query 5E Alternative
select DEP_ID, NUM_EMPLOYEES, AVG_SALARY from
  ( select DEP_ID, COUNT(*) AS NUM_EMPLOYEES, AVG(SALARY) AS AVG_SALARY from EMPLOYEES group by DEP_ID)
  where NUM_EMPLOYEES < 4
order by AVG_SALARY;

-- Query 6
-- Utilizando duas tabelas
select * from Departments;
select * from Employees;
select D.Dep_name, E.F_name, E.L_name
	from Employees as E, Departments as D 
	where E.Dep_ID = D.Dept_ID_Dep
	order by D.Dep_name, E.L_name desc;








