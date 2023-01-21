DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS parking_spots;
DROP TABLE IF EXISTS reservations;


PRAGMA forein_keys = ON;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number INTEGER NOT NULL
);

CREATE TABLE parking_spots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lon REAL NOT NULL,
    lat REAL NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    owner_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month INTEGER NOT NULL,
    date INTEGER NOT NULL,
    parking_id INTEGER NOT NULL,
    reserver_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (parking_id) REFERENCES parking_spots(id),
    FOREIGN KEY (reserver_id) REFERENCES users(id),
    FOREIGN KEY (owner_id) REFERENCES users(id)
);
