""" 
SQL Challenges

Reference: https://pgexercises.com/

Table Schema: 

cd.members:
------------------------------------------------
memid: integer
surname: char(200)
firstname: char(200)
address: char(300)
zipcode: int 
telephone: char(20)
recommendedby: integer	
joindate: timestamp

cd.bookings:
------------------------------------------------
facid: integer
memid: integer
starttime: timestamp
slots: integer

cd.facilities:
------------------------------------------------
facid: integer
name: char(100)
membercost: numeric
guestcost: numeric
initialoutlay: numeric
monthlymaintenance: numeric
"""

--CRUD
---------------------------------------------------------------------------------------------------
-- Insert some data into a table
insert into cd.facilities
    (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
    values (9, 'Spa', 20, 30, 100000, 800);   

-- Update a record
update cd.facilities
    set initialoutlay = 10000
    where facid = 1;     

-- REGEX
---------------------------------------------------------------------------------------------------
-- produce a list of all facilities with the word 'Tennis' in their name?
select * from cd.facilities
where name like '%Tennis%'


-- CASE STATEMENTS
---------------------------------------------------------------------------------------------------
-- produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.

select name, 
	case when (monthlymaintenance > 100) then 'expensive'
	else 'cheap'
	end as cost
from cd.facilities 


--AGGREGATES
--------------------------------------------------------------------------------------------------- 

-- You'd like to get the signup date of your last member. How can you retrieve
-- this information?

select max(joindate) as latest
	from cd.members;      

-- Produce a list of the total number of slots booked per facility. produce an output table consisting of facility id and slots, sorted by facility id.

select facid, sum(slots) as "Total Slots" from cd.bookings
	group by facid
	order by facid asc

-- Produce a list of the total number of slots booked per facility in the month
-- of September 2012. Produce an output table consisting of facility id and
-- slots, sorted by the number of slots.

select facid, sum(slots) as "Total Slots" 
	from cd.bookings
	where starttime >= '2012-09-01' and starttime < '2012-10-01'
	group by facid
	order by "Total Slots" asc

-- Produce a list of facilities with more than 1000 slots booked. Produce an
-- output table consisting of facility id and slots, sorted by facility id.

select facid, sum(slots) as "Total Slots"
	from cd.bookings
	group by facid
	having sum(slots) > 1000
	order by facid



-- SUBQUERIES
--------------------------------------------------------------------------------------------------- 
-- How can you produce a list of all members who have used a tennis court?
select distinct(m.firstname || ' ' || m.surname) as member, 
m.name as facility from
(
  select * from cd.members as mem
	inner join cd.bookings as b on b.memid=mem.memid
	inner join cd.facilities as f on f.facid=b.facid
  	where name like '%Tennis Court%'
) as m
order by member,facility


-- produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30?
select x.member, x.facility, x.cost from 
(select m.firstname || ' ' || m.surname as member, 
	   f.name as facility, 
	   case when (m.memid = 0) then
				  	b.slots * f.guestcost
				  else
				 	 b.slots * f.membercost
		end as cost
from cd.members as m 
inner join cd.bookings as b on b.memid=m.memid
inner join cd.facilities as f on f.facid=b.facid
where b.starttime >= '2012-09-14' and  b.starttime < '2012-09-15') as x
where x.cost > 30 
order by cost desc


-- DATES
--------------------------------------------------------------------------------------------------- 
-- Return a count of bookings for each month, sorted by month
select date_trunc('month',starttime) as month, count(*)
	from cd.bookings
	group by month
	order by month