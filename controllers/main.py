from flask import *

from extensions import connect_to_database

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def main_hello():
    # db = connect_to_database()
    # cur = db.cursor()
    # cur.execute('SELECT username, firstname FROM User')
    # results = cur.fetchall()

    return render_template("index.html")
