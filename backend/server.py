from flask import Flask, request, jsonify
from flask_managers import User_Manager, Book_Manager, Park_Manager
from db import Db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
port = 1999
db = None
user_manager = None
book_manager = None
park_manager = None
db_name = 'database.db'


@app.route('/user', methods=['GET', 'POST'])
def user():
    # if http method is not compatible for this endpoint, sends a json status response
    if request.method == 'GET':
        # do user authentication and return a satus report
        # args needs username and password
        args = request.args
        username = args.get('username', "")
        password = args.get('password', "")

        if "" in [username, password]:
            return jsonify(status="error", message="non-compatible request made to /user")

        return user_manager.check_user_authentication(username, password)

    elif request.method == 'POST':
        # add new user to database
        # payload needs username, password, email, first_name, last_name
        # anf phonenumber
        user_data = request.get_json(force=True)
        username = user_data.get('username', "")
        password = user_data.get('password', "")
        email = user_data.get('email', "")
        first_name = user_data.get('first_name', "")
        last_name = user_data.get('last_name', "")
        phone_number = user_data.get('phone_number', "")

        if "" in [username, password, email, first_name, last_name, phone_number]:
            return jsonify(status="error", message="non-compatible request made to /user")

        return user_manager.add_new_user(username, password, email, first_name, last_name, phone_number)

    return jsonify(status="error", message="non-compatible request made to /user")


@app.route('/book', methods=['GET', 'POST'])
def book():
    # if http method is not compatible for this endpoint, sends a json status response
    if request.method == 'GET':
        # check if there is a booking and return the data for that booking
        # args needs booking_id
        args = request.args
        booking_id = args.get('booking_id')

        if "" in [booking_id]:
            return jsonify(status="error", message="non-compatible request made to /book")

        return book_manager.get_booking(booking_id)

    elif request.method == 'POST':
        # add a new booking to the database, booking_id is created by us
        # payload needs date, parking_id, user_id
        # where user_id is the id of the user booking the parking stall
        booking_data = request.get_json(force=True)
        date = booking_data.get('date', "")
        parking_id = booking_data.get('parking_id', "")
        user_id = booking_data.get('user_id')

        if "" in [date, parking_id, user_id]:
            return jsonify(status="error", message="non-compatible request made to /book")

        return book_manager.book_parking_stall(date, parking_id, user_id)

    return jsonify(status="error", message="non-compatible request made to /book")


@app.route('/park', methods=['GET', 'POST'])
def park():
    # if http method is not compatible for this endpoint, sends a json status response
    if request.method == 'GET':
        # either gets all parking
        # args needs either
        # type which is "all", place with city/country
        # type which is "single" and parking_id
        args = request.args
        type = args.get('type', "")
        if type == "all":
            # get all parking stalls with the given time and datae available for the given place
            place = args.get('place', "")

            if "" in [place]:
                return jsonify(status="error", message="non-compatible request made to /park")

            return park_manager.get_all_parking_with(place)
        elif type == "single":
            # get a singe parking stall with the gicen parking_id
            parking_id = args.get('parking_id', "")

            if "" in [parking_id]:
                return jsonify(status="error", message="non-compatible request made to /park")

            return park_manager.get_parking_stall(parking_id)
        else:
            # if there was no type specified
            return jsonify(status="error", message="non-compatible request made to /park")

    elif request.method == 'POST':
        # add a new parking stall to the database, parking \_id is created by us
        # payload needs user_id, latitude, longitude, image_url, place, price, description
        # where user_id is the id of the user posting their own parking stall
        parking_data = request.get_json(force=True)
        
        longitude = parking_data.get('long', "")
        latitude = parking_data.get('lat', "")
        address = parking_data.get('address', "")
        city = parking_data.get('city', "")
        country = parking_data.get('country', "")
        description = parking_data.get('description', "")
        price = parking_data.get('price', "")
        user_id = parking_data.get('user_id', "")
        image_url = parking_data.get('image_url', "")
        

        if "" in [longitude, latitude, address, city, country, description, price, user_id, image_url]:
            return jsonify(status="error", message="non-compatible request made to /park")

        return park_manager.add_parking_stall(longitude, latitude, address, city, country, description, price, user_id, image_url)

    return jsonify(status="error", message="non-compatible request made to /park")


if __name__ == "__main__":
    db = Db(db_name)
    db.init_db()
    db.insert_sample()

    user_manager = User_Manager(db)
    book_manager = Book_Manager(db)
    park_manager = Park_Manager(db)

    app.run(port=port)
