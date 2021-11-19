-- Classes More Than 5 Students

-- Reference: https://leetcode.com/problems/classes-more-than-5-students/

-- SQL Schema
-- There is a table courses with columns: student and class

-- Please list out all classes which have more than or equal to 5 students.

-- For example, the table:

-- +---------+------------+
-- | student | class      |
-- +---------+------------+
-- | A       | Math       |
-- | B       | English    |
-- | C       | Math       |
-- | D       | Biology    |
-- | E       | Math       |
-- | F       | Computer   |
-- | G       | Math       |
-- | H       | Math       |
-- | I       | Math       |
-- +---------+------------+
-- Should output:

-- +---------+
-- | class   |
-- +---------+
-- | Math    |
-- +---------+

# Write your MySQL query statement below
select a.class from 
    (select class, count(distinct student) as n_students 
        from courses) as a
where a.n_students >= 5