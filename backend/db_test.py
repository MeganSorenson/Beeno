from flask import Flask, render_template, request, url_for, flash, redirect
from markupsafe import escape
from db import Db
import sqlite3

app = Flask(__name__)
db = None
db_name = 'database.db'
port = 3001

db = Db(db_name)
db.init_db()
db.insert_sample()

app.run(port = port)