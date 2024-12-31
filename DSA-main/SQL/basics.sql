Select top(10) * from user_table;

Select name, salary from employees
order by salary desc limit 10;

Select e.id as employees_id, t.id as team_id, t.team_name
from employees e 
inner join teams t 
on e.team_id=t.id;

Select position, count(*) as num_employees 
from employees 
group by position;

SELECT *
FROM employee_table
WHERE employment_type = 'salaried'
ORDER BY hire_date
LIMIT 1 OFFSET n - 1;

Select max(num) num from (
Select num from mynumbers
group by num Having count(num)=1
) as unique_numbers
;

