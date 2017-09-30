from flask import *
from extensions import connect_to_database

reflection = Blueprint('reflection', __name__, template_folder='templates')


@reflection.route('/reflection', methods=['GET', 'POST'])
def reflection_route():
    db = connect_to_database()
    cur = db.cursor()
    if request.method == "POST":
        response = request.form.get("reflectionform")

    	cur.execute('INSERT INTO Blogs (Username, Content, Type) Values (%s, %s,%s);', ('doej', response, 'share'))
        db.close()
	return render_template("index.html")

    return render_template("reflection.html")

    #If method = Post 
    	#record reflection for student and add to table

@reflection.route('/feedback', methods=['GET', 'POST'])
def feedback_route():
	db = connect_to_database()
	cur = db.cursor()

	if request.method == "POST":
		f1 = request.form.get("feedback")
		print type(f1)
		f2 = request.form.get("feedback1")
		print type(f2)
		f3 = request.form.get("feedback2")
		print type(f3)
		f4 = request.form.get("feedback3")
		print type(f4)
		f5 = request.form.get("feedback4")
		print type(f5)
		f6 = request.form.get("feedback5")
    		print type(f6)
		f7 = request.form.get("feedback6")
		print type(f7)
    		cur.execute('INSERT INTO Feedback (JourneyID, Scale, Reason, Positive, Addition, Lesson, Person, Intersting) Values(%s, %s, %s,%s, %s,%s, %s,%s);',(1,f1, f2, f3,f4,f5,f6, f7))

		return render_template("index.html")
    	return render_template("feedback.html")
