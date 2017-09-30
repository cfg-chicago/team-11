from flask import *

from extensions import connect_to_database

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/login', methods=['GET', 'POST'])
def main_login():
    if request.method == 'POST':
        uname = request.form.get('uname')
        psw = request.form.get('psw')

        if (check_login(uname, psw)):
            return render_template("index.html", uname=uname)

    return render_template('login.html')

@main.route('/')
def main_hello():
    # db = connect_to_database()
    # cur = db.cursor()
    # create_table_queries = open("create_tables.sql", "r")
    # cur.execute(create_table_queries)
    # results = cur.fetchall()

    return render_template("index.html")

def check_login(uname, psw):
    db = connect_to_database()
    cur = db.cursor()
    cur.execute('SELECT Password FROM USERS WHERE Username="%s";', uname)
    results = cur.fetchall()

    return results == psw
