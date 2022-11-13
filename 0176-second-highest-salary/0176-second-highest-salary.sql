Select Max(Salary) As 'SecondHighestSalary'
From Employee
where Salary < (Select Max(Salary)
From Employee);