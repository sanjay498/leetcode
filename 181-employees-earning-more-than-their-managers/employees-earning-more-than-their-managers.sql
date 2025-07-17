SELECT e.name AS employee
FROM employee As e
JOIN employee AS m
ON e.managerId = m.id
WHERE e.salary > m.salary;
