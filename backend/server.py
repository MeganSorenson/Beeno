from flask import Flask, request, jsonify
from flask_managers import User_Manager, Book_Manager, Park_Manager

app = Flask(__name__)
port = 1999


@app.route('/user', methods=['GET', 'POST'])
def user():
    # if http method is not compatible for this endpoint, sends a json status response
    manager = User_Manager()

    if request.method == 'GET':
        # do user authentication and return a satus report
        # args needs username and password
        args = request.args()
        username = args.get('username', "")
        password = args.get('password', "")

        if "" in [username, password]:
            return jsonify(status="error", message="non-compatible request made to /user")

        return manager.check_user_authentication(username, password)

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

        return manager.add_new_user(username, password, email, first_name, last_name, phone_number)

    return jsonify(status="error", message="non-compatible request made to /user")


@app.route('/book', methods=['GET', 'POST'])
def book():
    # if http method is not compatible for this endpoint, sends a json status response
    manager = Book_Manager()

    if request.method == 'GET':
        # check if there is a booking and return the data for that booking
        # args needs booking_id
        args = request.args()
        booking_id = args.get('booking_id')

        if "" in [booking_id]:
            return jsonify(status="error", message="non-compatible request made to /book")

        return manager.get_booking(booking_id)

    elif request.method == 'POST':
        # add a new booking to the database, booking_id is created by us
        # payload needs day, month, parking_id, user_id
        # where user_id is the id of the user booking the parking stall
        booking_data = request.get_json(force=True)
        day = booking_data.get('day', "")
        month = booking_data.get('month', "")
        parking_id = booking_data.get('parking_id', "")
        user_id = booking_data.get('user_id')

        if "" in [day, month, parking_id, user_id]:
            return jsonify(status="error", message="non-compatible request made to /book")

        return manager.book_parking_stall(day, month, parking_id, user_id)

    return jsonify(status="error", message="non-compatible request made to /book")


@app.route('/park?type=all', methods=['GET', 'POST'])
def park():
    # if http method is not compatible for this endpoint, sends a json status response
    manager = Park_Manager()

    if request.method == 'GET':
        # either gets all parking
        # args needs either
        # type which is "all", place with city/country, day, and month ... or
        # type which is "single" and parking_id
        args = request.args
        type = args.get('type', "")
        if type == "all":
            # get all parking stalls with the given time and datae available for the given place
            place = args.get('place', "")
            day = args.get('day', "")
            month = args.get('month', "")

            if "" in [place, day, month]:
                return jsonify(status="error", message="non-compatible request made to /park")

            return manager.get_all_parking_with(place, day, month)
        elif type == "single":
            # get a singe parking stall with the gicen parking_id
            parking_id = args.get('parking_id', "")

            if "" in [parking_id]:
                return jsonify(status="error", message="non-compatible request made to /park")

            return manager.get_parking_stall(parking_id)
        else:
            # if there was no type specified
            return jsonify(status="error", message="non-compatible request made to /park")

    elif request.method == 'POST':
        # add a new parking stall to the database, parking \_id is created by us
        # payload needs user_id, latitude, longitude, image_url, place, price, description
        # where user_id is the id of the user posting their own parking stall
        parking_data = request.get_json(force=True)
        user_id = parking_data.get('user_id', "")
        latitude = parking_data.get('lat', "")
        longitude = parking_data.get('long', "")
        image_url = parking_data.get('image_url', "")
        place = parking_data.get('place', "")
        price = parking_data.get('price', "")
        description = parking_data.get('desc', "")

        if "" in [user_id, latitude, longitude, image_url, place, price, description]:
            return jsonify(status="error", message="non-compatible request made to /park")

        return manager.add_parking_stall(user_id, latitude, longitude, image_url, place, price, description)

    return jsonify(status="error", message="non-compatible request made to /park")
