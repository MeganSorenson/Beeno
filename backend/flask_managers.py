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
            "SELECT * FROM reservations WHERE date=? AND parking_id=?", (date,parking_id))
        rows = cur.fetchall()

        if len(rows) >= 1:
            return jsonify(status="error", message="parking space already taken")
        else:
            cur.execute(
                "INSERT INTO reservations (date,parking_id,reserver_id) VALUES (?,?,?);",
                (date,parking_id,user_id,))
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

    def add_parking_stall(self, user_id, latitude, longitude, image_url, place, price, description):
        # returns a json object with "status" that is either "success" or "error"
        # and "message" that is a description of the status
        pass
