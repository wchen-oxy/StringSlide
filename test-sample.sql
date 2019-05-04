###### SAMPLE INSERT STATEMENTS ######
Insert Into Guitar(guitar_id, manufacturer_name, guitar_name, guitar_model, serial_number)
Values("55", "Airline", "JB Hutto", "Montgomery Ward", "JBH03171964"); 

Insert Into Story(story_id, guitar_id, story, where_purchased, custom_built)
Values("175", "55", "Joe Strummer was playing with the 101ers when he bought his 1966 Fender Telecaster in 1975 for £120. After joining the Clash, the guitar's body and pickguard were refinished in grey auto primer and then painted black. By 1979, the word NOISE was stenciled on the upper part of the body, a rasta flag sticker was placed at the horn of the pickguard, and an "Ignore Alien Orders" sticker was placed above the bridge. By the release of Give 'Em Enough Rope, the guitar was fitted with a bridge with individual saddles and the original Kluson tuners were replaced with later model tuners and a large question mark was spraypainted on its back. The guitar would remain in this configuration throughout his career with the addition of different stickers on its body. The guitar's black paint became worn down due to Strummer's playing and on many places the original sunburst finish and bare wood shines through, except for the square where Strummer taped his setlists. Strummer was naturally left-handed, but learned to play guitar right-handed. He had attributed this as a drawback and claimed it caused him to be underdeveloped as a guitarist, although his style of playing was unique. Fender guitars have since released a Joe Strummer Signature Telecaster Model designed in cooperation with the Strummer estate.", "Detroit, United States", "FALSE");

Insert Into Photos(guitar_id, photo_number, photo_path) 
Values("55", "34", "https://imgur.com/a/KOshC2N");

Insert Into Videos(guitar_id, photo_number, photo_path) 
Values("55", "34", "https://www.youtube.com/watch?v=O4iGNXsqghs");

Insert Into Specs(guitar_id, production_year, weight, finish, body_wood, neck_wood, fretboard_wood, cap_wood, neck_pickup, middle_pickup, bridge_pickup, repairs)
Values("87","1986","10.5","Amber","Mahogany","Mahogany","Brazilian Rosewood","Maple","Seymour Duncan APH1",NULL,"Seymour Duncan APH1",TRUE);

Insert Into Appearances(guitar_id, tour_name, album_name)
Values("87","Appetite for Destruction Tour","Appetite for Destruction");

###### SAMPLE SELECT STATEMENT USED TO LOAD INFORMATION ON WEBSITE ######
###### QUERY RESULTS FROM test-sample.out ARE FROM ALL QUERIES FROM DOWN BELOW IN SAME ORDER #######
# Load the manufacturer name, the model of the guitar, when it was made, and its picture
Select manufacturer_name, guitar_model, production_year, photo_path 
from Guitar g inner join Specs s on g.guitar_id = s.guitar_id 
inner join Photos p on g.guitar_id = s.guitar_id 
where guitar_id="100";

# Load the video for the guitar with ID 100
Select video_path 
from Videos 
where guitar_id="100";

# Find the woods used on the guitar with ID 100
Select body_wood, neck_wood, fretboard_wood, cap_wood 
from Specs 
where guitar_id="100";

# ALLOW USER TO CHANGE THE NAME OF THEIR GUITAR
select guitar_name 
from Guitar 
where guitar_id="45";

Update Guitar 
set guitar_name="The Cool One" 
where guitar_id="45";

# Allow user to see how many Guitar from each Brand there are in the website
select manufacturer_name, count(guitar_model) 
from Guitar 
group by manufacturer_name;

####### SAMPLE INTEREST SELECT STATEMENTS ######
# Find all the Gibson guitars that were made in 1945
Select manufacturer_name, guitar_model, production_year from Guitar g 
inner join Specs s on g.guitar_id=s.guitar_id 
where g.manufacturer_name="Gibson" 
and s.production_year="1945";

# Find all the Fender guitars that were made before 1980
Select manufacturer_name, guitar_model, production_year 
from Guitar g inner join Specs s on g.guitar_id = s.guitar_id 
where g.manufacturer_name="Fender" AND s.production_year<1980;

# Find all the stories from Gibson Les Paul Customs
Select story_text, guitar_name
from Story s inner join Guitar g on s.guitar_id=g.guitar_id 
inner join Specs t on g.guitar_id=t.guitar_id 
where guitar_name="Raspy Sounds" and production_year="1976";

# Find all the original 1959 Les Pauls that where purchased in Europe
Select guitar_model, production_year, where_purchased 
from Guitar g inner join Story s on g.guitar_id=s.guitar_id 
inner join Specs t on s.guitar_id=t.guitar_id 
where s.where_purchased like '%Bria%';