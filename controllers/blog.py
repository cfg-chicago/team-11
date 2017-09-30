from flask import *
from extensions import connect_to_database

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/blog', methods=['GET', 'POST'])
def reflection_route():
    db = connect_to_database()
    cur = db.cursor()
    t = 'share'    
    cur.execute('SELECT * FROM Blog WHERE Type="share";')
    blog_posts = cur.fetchall()
    cur.execute('SELECT FirstName,LastName,UserID FROM User;')
    users = cur.fetchall

    print blog_posts
    for blog in blog_posts:
    	userid = blog['UserID']
    	for user in users:
    		if userid == user['UserID']:
    			blog['firstname'] = user['FirstName']
    			blog['lastname'] = user['lastname']

    options = {"blog_posts":blog_posts}
    return render_template("blog.html", **options)
