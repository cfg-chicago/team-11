from flask import *

from extensions import connect_to_database

reflection = Blueprint('reflection', __name__, template_folder='templates')


@reflection.route('/reflection')
def reflection_route():
    # db = connect_to_database()
    # cur = db.cursor()
    # cur.execute('SELECT username, firstname FROM User')
    # results = cur.fetchall()
    return render_template("reflection.html")

    #If method = Post 
    	#record reflection for student and add to table

    