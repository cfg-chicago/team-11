from flask import *

from extensions import connect_to_database

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/login', methods=['GET', 'POST'])
def main_login():
    if request.method == 'POST':
        uname = request.form.get('uname')
        print (uname)
        psw = request.form.get('psw')
        print (psw)
        print('POST WAS RECEIVED')

        if check_login(uname,psw):
            return render_template("index.html", uname=uname)
        else:
            return "anything"


    return render_template('login.html', uname='$USER')

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
    cur.execute('SELECT Password FROM Users WHERE Username="%s";', uname)
    results = cur.fetchall()
    print(results)

    return results[0]["Password"] == psw
