SELECT (MONTHS*SALARY) AS EARNINGS, COUNT(MONTHS*SALARY) FROM EMPLOYEE
GROUP BY EARNINGS
ORDER BY EARNINGS DESC
LIMIT 1;


#Explanation:
salary*month --- first to calculate total earnings we multiply month * salary

count() -- next for counting no of employees having that salary we use count()

group by 1 -- ill take simple example..consider query SELECT name , id FROM employee group by 1; in this query there are 2 columns i.e., name and id...So we have to group it by 1st column that is name.

order by earning desc -- it will order the table in desc order do that max value appears frst.

limit 1 -- it will limit the table to 1 row only. so the query displays the frst row only.
