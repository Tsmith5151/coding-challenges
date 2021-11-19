-- Reference: https://www.hackerrank.com/challenges/more-than-75-marks/problem

-- Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.


select Name from STUDENTS where Marks > 75
order by SUBSTRING(NAME, -3), ID ASC


-- Reference: https://www.hackerrank.com/challenges/weather-observation-station-7/problem

-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.


SELECT City
FROM Station
WHERE City REGEXP '^[aeiou]' and City REGEXP '[aeiou]$';


-- Reference: https://www.hackerrank.com/challenges/weather-observation-station-9/problem

-- Query the list of CITY names from STATION that do not start with vowels.
-- Your result cannot contain duplicates.

SELECT  Distinct(City)
FROM Station
WHERE City NOT REGEXP '^[aeiou]'