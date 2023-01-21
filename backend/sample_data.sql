INSERT INTO users (username,password,first_name,last_name,email,phone_number) VALUES ('user1','password1','first1','last1','user1@beeno.com',11111111111);
INSERT INTO users (username,password,first_name,last_name,email,phone_number) VALUES ('user2','password2','first2','last2','user2@beeno.com',22222222222);
INSERT INTO users (username,password,first_name,last_name,email,phone_number) VALUES ('user3','password3','first3','last3','user3@beeno.com',33333333333);

INSERT INTO parking_spots (lon,lat,address,city,country,description,owner_id,price,image_url) VALUES (1,1,'address1','city1','country1','description1',111,1,"https://img.atlasobscura.com/RUfqbarn7ccWAnhV9hjYDul5FhDiVUnxTL8rCM03xqM/rt:fit/w:600/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS91/cGxvYWRzL3BsYWNl/X2ltYWdlcy81N2M1/ZWJkNDE5YmI3Y2M3/N2JfQXBwbGVfR2Fy/YWdlLmpwZw.jpg");

INSERT INTO reservations (date, parking_id,reserver_id,owner_id) VALUES ('2023-01-31',1,1,2);
