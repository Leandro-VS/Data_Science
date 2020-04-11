select * from PETSALE;
select Sum(Saleprice) from PETSALE;
select MIN(Saleprice) from PETSALE;
select ROUND(Saleprice) from Petsale;
select DAY(Saledate) from Petsale where Animal = 'cat';
select Count(*) from Petsale where MONTH(Saledate) = '06';

--Sub-Querys
select EMP_ID, F_name, L_name, Salary from Employees
where Salary < (select AVG(salary) from Employees);

--Multiple tables 
select * from Employees
	where Dep_ID IN (select Dept_ID_Dep from Departments);

--Implicit JOIN 
select * from Employees, Departments;

--Limitadores
select * from Employees, Departments
	where Employees.Dep_ID = Departments.Dept_ID_Dep;
	
--Prefixos
select * from Employees E, Departments D
where E.Dep_ID = D.Dept_ID_Dep;