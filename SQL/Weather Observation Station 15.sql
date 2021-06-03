SELECT ROUND(LONG_W, 4) FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC 
LIMIT 1;

#The MAX() must be followed by either GROUP/ORDER/...etc(ORDER BY in this case)for the query to work.
