# Write your MySQL query statement below
select b.name as Employee  from Employee as A inner join Employee as B on A.id = B.managerId where b.salary > a.salary
