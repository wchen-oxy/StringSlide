-- Find all the guitars in the website that were made in 1976
Select manufacturer_name, guitar_model, guitar_name
from Story s inner join Guitar g on s.guitar_id=g.guitar_id
inner join Specs t on g.guitar_id=t.guitar_id
where production_year=1976;

-- Any guitar that is made before 1989 is considered vintage.
-- Find all the guitars that were made by Gibson prior to 1989
Select manufacturer_name, guitar_model, production_year
from Guitar g inner join Specs t
on g.guitar_id=t.guitar_id
where manufacturer_name="Gibson" and production_year<1989;

-- find any vintage guitar that is currently located in Korea
Select manufacturer_name, guitar_model, guitar_name, production_year
from Story s inner join Guitar g on s.guitar_id=g.guitar_id
inner join Specs t on g.guitar_id=t.guitar_id
where where_purchased like '%Korea%' and production_year<1989;

-- return a list of the number of guitars made by each manufacturer
-- that is in the database
-- replace the manufacturer_name to know figure out how manually
-- guitars are made by a specific manufacturer
select manufacturer_name, count(*)
from guitar
where manufacturer_name='Gibson'
group by manufacturer_name
having count(*);

-- give the guitar_model and production_year of the oldest
-- guitars that are present in the dataset
select guitar_model, production_year
from specs, guitar
where guitar.guitar_id=specs.guitar_id
and production_year = (select min(production_year) from specs);
-- change from min to max if you want to find the newest guitars

-- find the location of the all the guitars made by
-- gibson in 1950s
-- or change the
select manufacturer_name, guitar_model, production_year, where_purchased
from guitar g inner join specs s on g.guitar_id=s.guitar_id
inner join story t on s.guitar_id=t.guitar_id
where s.production_year like '195%' and g.manufacturer_name='Gibson';

-- find all the fender guitars made in 1963
-- and where they are located right know
select manufacturer_name, guitar_model, production_year, where_purchased
from guitar g inner join specs s on g.guitar_id=s.guitar_id
inner join story t on s.guitar_id=t.guitar_id
where s.production_year=1963 and g.manufacturer_name='Fender';

-- check the pickups on all the stratocaster guitars
select manufacturer_name, guitar_model, production_year, neck_pickup, middle_pickup, bridge_pickup
from guitar g inner join specs s on g.guitar_id=s.guitar_id
where manufacturer_name="Fender" and guitar_model="Stratocaster";

-- find all the guitars that contain PAF pickups
-- the "holy grail" of guitar pickups
-- in either position
select manufacturer_name, guitar_model, production_year, neck_pickup, middle_pickup, bridge_pickup
from guitar g inner join specs s on g.guitar_id=s.guitar_id
where bridge_pickup="PAF" or neck_pickup="PAF" or middle_pickup="PAF";
