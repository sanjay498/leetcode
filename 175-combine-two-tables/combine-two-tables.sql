SELECT p.firstname, p.lastname, a.city, a.state
FROM person p 
left JOIN address a ON p.personid = a.personid;
