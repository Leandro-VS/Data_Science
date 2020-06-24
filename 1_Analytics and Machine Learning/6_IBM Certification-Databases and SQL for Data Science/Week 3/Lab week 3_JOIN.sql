select * from Employees;
select * from Job_history;
select * from Jobs;
select * from Departments;

--Query 1A
select E.F_name, E.L_name, J.Start_date from Employees E  
	INNER JOIN Job_history J ON E.Emp_ID = J.Empl_ID
	where E.Dep_ID = 5;
	
--Query 1B
--Relações Employees -> Job_History e Employees -> Jobs
select E.F_name, E.L_name, JH.Start_date, J.Job_Title from Employees E 
	INNER JOIN Job_history JH ON  E.Emp_ID = JH.Empl_ID
	INNER JOIN Jobs J ON E.Job_ID = J.Job_ident
	where  E.Dep_ID = '5';
	
--Query 2A
select E.Emp_ID, E.L_name, E.Dep_ID, D.Dep_name from Employees E 	
	Left JOIN Departments D ON E.Dep_ID = D.Dept_ID_Dep;
	
--Query 2B
select E.Emp_ID, E.L_name, E.Dep_ID, E.B_date, D.Dep_name from Employees E 	
	Left JOIN Departments D ON E.Dep_ID = D.Dept_ID_Dep
	where Year(E.B_date) < 1980;
	
--Query 2C
select E.Emp_ID, E.L_name, E.Dep_ID, D.Dep_name, E.B_date from Employees E 	
	Left JOIN Departments D ON E.Dep_ID = D.Dept_ID_Dep AND Year(E.B_date) < 1980;	
	
--Query 3A
select E.F_name, E.L_name, D.Dep_name from Employees E 
	FULL JOIN Departments D ON E.Dep_ID = D.Dept_ID_Dep;	
	
--Query 3B
select E.F_name, E.L_name, D.Dept_ID_Dep, D.Dep_name  from Employees E 
	FULL JOIN Departments D ON E.Dep_ID = D.Dept_ID_Dep
	AND E.Sex = 'M';
	
	
	
	
	
	
	
	
	