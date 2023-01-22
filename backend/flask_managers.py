from flask import jsonify
import json


class User_Manager:
    # creates a user manager that encapsulates the functionality of an http request to /user
    def __init__(self, db):
        self.db = db

    def check_user_authentication(self, username, password):
        # checks the database if the username and the password match
        # returns a json object with "status" that is either "success" or "error"
        # and "message" that is a description of the status
        cur = self.db.cur
        cur.execute(
            "SELECT * from users WHERE username=? and password=?", (username, password,))

        rows = cur.fetchall()

        if len(rows) == 1:
            return jsonify(status="success", message="login successful")
        else:
            return jsonify(status="error", message="invalid username or password, login unsuccesful")

    def add_new_user(self, username, password, email, first_name, last_name, phone_number):
        # adds new user to the database with the given user_info
        # returns a json object with "status" that is either "success" or "error"
        # and "message" that is a description of the status
        cur = self.db.cur

        cur.execute(
            "SELECT * from users WHERE username=?", (username,))
        rows = cur.fetchall()

        if len(rows) >= 1:
            return jsonify(status="error", message="username already taken")
        else:
            cur.execute(
                "INSERT INTO users (username,password,first_name,last_name,email,phone_number) VALUES (?,?,?,?,?,?)",
                (username, password, first_name, last_name, email, int(phone_number),))
            self.db.conn.commit()
            return jsonify(status="success", message="insert successful")


class Book_Manager:
    # creates a user manager that encapsulates the functionality of an http request to /book
    def __init__(self, db):
        self.db = db

    def get_booking(self, booking_id):
        # checks if there is a booking in the database with the given booking_id
        # returns a json of the booking with the given booking_id
        # or json status update with "status" that is "error" and "message" that is a description of the error
        cur = self.db.cur
        cur.execute("SELECT * from reservations WHERE id=?", (booking_id))

        rows = cur.fetchall()

        if len(rows) == 1:
            data = rows[0]
            id = data[0]
            date = data[1]
            parking_id = data[2]
            reserver_id = data[3]
            owner_id = data[4]

            return jsonify(booking_id=id, booking_date=date,
                           parking_id=parking_id, reserver_id=reserver_id,
                           stall_owner_id=owner_id)
        else:
            return jsonify(status="error", message="no booking with given id")

    def book_parking_stall(self, date, parking_id, user_id):
        # checks if there is already a booking for the given parking_id with the given date
        # returns a json object with "status" that is either "success" or "error"
        # and "message" that is a description of the status
        cur = self.db.cur

        cur.execute(
            "SELECT * FROM reservations WHERE date=? AND parking_id=?", (date, parking_id))
        rows = cur.fetchall()

        if len(rows) >= 1:
            return jsonify(status="error", message="parking space already taken")
        else:
            cur.execute(
                "INSERT INTO reservations (date,parking_id,reserver_id) VALUES (?,?,?);",
                (date, parking_id, user_id,))
            self.db.conn.commit()
            return jsonify(status="success", message="insert successful")


class Park_Manager:
    # creates a park manager that encapsulates the functionality of an http request to /park
    def __init__(self, db):
        self.db = db

    def get_all_parking_with(self, place):
        # filters through database for ony prking stalls in the given place
        # place must be given as City,Country (no space)
        # returns a json with all those parking stalls that were filtered
        cur = self.db.cur

        place = place.split(",")
        city = place[0]
        country = place[1]

        rows = cur.execute(
            "SELECT * from parking_spots WHERE city=? and country=?", (city, country,))
        rows_dict = {}

        for row in rows:
            id = row[0]
            data = {
                "lon": row[1],
                "lat": row[2],
                "address": row[3],
                "place": row[4] + ", " + row[5],
                "description": row[6],
                "price": row[7],
                "owner_id": row[8],
                "image_url": row[9]
            }
            rows_dict[id] = data

        return json.dumps(rows_dict, indent=4)

    def get_parking_stall(self, parking_id):
        # checks if there is a parking_stall in the database with the given parking_id
        # returns a json of the parking with the given parking_id
        # or json status update with "status" that is "error" and "message" that is a description of the error
        cur = self.db.cur
        cur.execute(
            "SELECT * from parking_spots WHERE id=?", (parking_id,))

        rows = cur.fetchall()

        if len(rows) == 1:
            row = rows[0]
            id = row[0]
            data = {
                id: {
                    "lon": row[1],
                    "lat": row[2],
                    "address": row[3],
                    "place": row[4] + ", " + row[5],
                    "description": row[6],
                    "price": row[7],
                    "owner_id": row[8],
                    "image_url": row[9]
                }
            }
            return json.dumps(data, indent=4)
        else:
            return jsonify(status="error", message="no parking stall with given id")

    def get_users_stalls(self, user_id):
        # checks if there is a parking stall in the database for the given user_id
        # returns a json of all the parking stalls with the given user_id with keys being the parking_id
        cur = self.db.cur
        cur.execute("SELECT * from parking_spots WHERE owner_id=?", (user_id,))

        rows = cur.fetchall()
        rows_dict = {}

        for row in rows:
            id = row[0]
            data = {
                "lon": row[1],
                "lat": row[2],
                "address": row[3],
                "place": row[4] + ", " + row[5],
                "description": row[6],
                "price": row[7],
                "image_url": row[9]
            }
            rows_dict[id] = data

        return json.dumps(rows_dict, indent=4)

    def get_users_reservations(self, user_id):
        # checks if there is a reservation in the database for the given user_id (where user_id is stall owner)
        # returns a json of all the reservations with the given user_id with keys being the reservation_id
        parking_ids = self.get_parking_ids_for_user(user_id)
        result_dict = {}

        for id in parking_ids:
            cur = self.db.cur
            cur.execute("SELECT * from reservations WHERE parking_id=?", (id,))

            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    p_id = row[0]
                    data = {
                        "date": row[1],
                        "parking_id": row[2],
                        "reserver_id": row[3]
                    }
                    result_dict[p_id] = data

        return json.dumps(result_dict, indent=4)

    def get_parking_ids_for_user(self, user_id):
        # returns a list of all the parking ids that the owner has offered
        cur = self.db.cur
        cur.execute("SELECT * from parking_spots WHERE owner_id=?", (user_id,))

        rows = cur.fetchall()
        rows_array = []

        for row in rows:
            id = row[0]
            rows_array.append(id)

        return rows_array

    def add_parking_stall(self, longitude, latitude, address, city, country, description, price, user_id, image_url):
        # returns a json object with "status" that is either "success" or "error"
        # and "message" that is a description of the status

        cur = self.db.cur

        cur.execute(
            "INSERT INTO parking_spots (lon,lat,address,city,country,description,price,owner_id,image_url) VALUES (?,?,?,?,?,?,?,?,?);",
            (longitude, latitude, address, city, country, description, price, user_id, image_url))

        self.db.conn.commit()
        return jsonify(status="success", message="insert successful")
