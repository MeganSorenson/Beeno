INSERT INTO users (username,password,first_name,last_name,email,phone_number) VALUES ('user1','password1','Megan','Sorenson','megan@email.com',123-456-7890);
INSERT INTO users (username,password,first_name,last_name,email,phone_number) VALUES ('user2','password2','Eric','Pien','eric@email.com',567-283-2847);

INSERT INTO parking_spots (lon,lat,address,city,country,description,owner_id,price,image_url) VALUES (49.26334482271202, -123.24730278169302,'2250 Health Sciences Mall','Vancouver','CA',
'I have a reserved parking stall in this parkade (stall 234). The stall is on a 20 degree incline and is covered.',1,0,
"https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=RWrXCP7JQ2wFZDD95G-fMQ&cb_client=search.gws-prod.gps&w=408&h=240&yaw=285.45602&pitch=0&thumbfov=100");

INSERT INTO parking_spots (lon,lat,address,city,country,description,owner_id,price,image_url) VALUES (49.26746850964168, -123.16446306390904,'2627 W 16th Ave','Vancouver','CA',
'This is one of a few parking stalls that I am offering in front my business. Try to be out by 7AM. No cover from the elements.',1,0,
"https://lh5.googleusercontent.com/p/AF1QipPnp1r0d3Oczva4zHy0EAa7ZeNy8ESgKmNKhDKy=w408-h544-k-no");

INSERT INTO parking_spots (lon,lat,address,city,country,description,owner_id,price,image_url) VALUES (49.26746850964168, -123.16446306390904,'2627 W 16th Ave','Vancouver','CA',
'This is one of a few parking stalls that I am offering in front my business. Try to be out by 7AM. No cover from the elements.',1,0,
"https://lh5.googleusercontent.com/p/AF1QipPnp1r0d3Oczva4zHy0EAa7ZeNy8ESgKmNKhDKy=w408-h544-k-no");

INSERT INTO parking_spots (lon,lat,address,city,country,description,owner_id,price,image_url) VALUES (49.26746850964168, -123.16446306390904,'2627 W 16th Ave','Vancouver','CA',
'This is one of a few parking stalls that I am offering in front my business. Try to be out by 7AM. No cover from the elements.',1,0,
"https://lh5.googleusercontent.com/p/AF1QipPnp1r0d3Oczva4zHy0EAa7ZeNy8ESgKmNKhDKy=w408-h544-k-no");

INSERT INTO parking_spots (lon,lat,address,city,country,description,owner_id,price,image_url) VALUES (49.23979430246682, -122.96585520347882,'6501 Deer Lake Ave','Burnaby','CA',
'We are temporarily closed, so there is room for some vans on our street. Try not to make too much noise becuase there are lots of families aorund.',2,0,
"https://lh5.googleusercontent.com/p/AF1QipOQWDmDjXmAQXVqB-mJeTmCjb40vphftoBMd7LK=w426-h240-k-no");

INSERT INTO parking_spots (lon,lat,address,city,country,description,owner_id,price,image_url) VALUES (49.189791323089, -122.86494827959747,'10289 129 St','Surrey','CA',
'Nice flat stall in front of a residential house. Please clean up your garbage!',2,0,
"https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=7v5KMLMo5UhuXSIXS9xSYQ&cb_client=search.gws-prod.gps&w=408&h=240&yaw=289.50037&pitch=0&thumbfov=100");

INSERT INTO parking_spots (lon,lat,address,city,country,description,owner_id,price,image_url) VALUES (49.15438261982669, -123.1248268745648,'8140 Garden City Rd','Richmond','CA',
'I manage this A&W and have a reserved manager parking stall. As long as your in no earlier than 9PM and out by 8AM you will be good.',2,0,
"https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=7v5KMLMo5UhuXSIXS9xSYQ&cb_client=search.gws-prod.gps&w=408&h=240&yaw=289.50037&pitch=0&thumbfov=100");




INSERT INTO reservations (date, parking_id,reserver_id) VALUES ('2023-03-13',1,2);
INSERT INTO reservations (date, parking_id,reserver_id) VALUES ('2023-03-14',1,2);
INSERT INTO reservations (date, parking_id,reserver_id) VALUES ('2023-03-15',1,2);

INSERT INTO reservations (date, parking_id,reserver_id) VALUES ('2023-02-01',5,1);
INSERT INTO reservations (date, parking_id,reserver_id) VALUES ('2023-03-13',6,1);