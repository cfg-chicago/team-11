from flask import *
from extensions import connect_to_database

reflection = Blueprint('reflection', __name__, template_folder='templates')


@reflection.route('/reflection', methods=['GET', 'POST'])
def reflection_route():
    db = connect_to_database()
    cur = db.cursor()
    if request.method == "POST":
        response = request.form.get("reflectionform")
	print response
    	cur.execute('INSERT INTO Blog (UserID, Content, Type) Values (%s, %s,%s);', (1, response, 'share'))
    db.close()
    # results = cur.fetchall()
    return render_template("reflection.html")

    #If method = Post 
    	#record reflection for student and add to table

    
