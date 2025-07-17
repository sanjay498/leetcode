SELECT distinct p.email AS Email
FROM person p
JOIN person as dup
ON p.email = dup.email AND p.id <> dup.id;
