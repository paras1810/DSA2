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

with org_hierarchy as(
    select employee_id as orig_employee_id,
    employee_name as orig_employee_name,
    employee_id, 
    employee_name,
    manager_id,
    salary,
    1 as org_level
    from employees
    UNION ALL
    Select P.orig_employee_id,
    P.orig_employee_name,
    CH.employee_id,
    CH.employee_name,
    CH.manager_id,
    CH.salary,
    P.org_level+1
    from org_hierarchy P, Employees CH
    where ch.manager_id=P.employee_id
),
CEO_hierarchy as(
    Select org_hierarchy.employee_id as SUB_employee_id,
    org_hierarchy.employee_name,
    org_hierarchy.org_level as sub_level
    from org_hierarchy, Employees
    where org_hierarchy.orig_employee_id=Employees.employee_id
    and Employees.manager_id is null
)
Select org_hierarchy.orig_employee_id as employee_id,
org_hierarchy.orig_employee_name as employee_name,
CEO_hierarchy.sub_level as "level",
count(*)-1 as team_size,
sum(org_hierarchy.salary) as budget
from org_hierarchy, CEO_hierarchy
where org_hierarchy.orig_employee_id=CEO_hierarchy.SUB_employee_id
group by org_hierarchy.orig_employee_id,
org_hierarchy.orig_employee_name,
CEO_hierarchy.sub_level
order by 3 asc, 5 desc, 2

with user_content_split as(
    Select content_id, CONCAT(UPPER(SUBSTRING(value,1,1)), LOWER(SUBSTRING(value,2,len(value)))) AS 'words'
    from user_content 
    CROSS Apply STRING_SPLIT(REPLACE(content_text, '-', ' _ '), ' ') 
)
Select ucs.content_id as 'content_id', content_text as 'original_text', REPLACE(STRING_AGG(words,' '),' - ', '-') as 'converted_text'
from user_content_split ucs join user_content uc on ucs.content_id=uc.content_id 
group by ucs.content_id, content_text 
order by content_id

