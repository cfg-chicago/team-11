from flask import *
from extensions import connect_to_database

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/blog', methods=['GET', 'POST'])
def blog_route():
    db = connect_to_database()
    cur = db.cursor()
    t = 'share'    
    cur.execute('SELECT * FROM Blogs WHERE Type="share";')
    blog_posts = cur.fetchall()
    cur.execute('SELECT FirstName,LastName,Username FROM Users;')
    users = cur.fetchall()

    print blog_posts
    for blog in blog_posts:
    	userid = blog['Username']
    	for user in users:
    		if userid == user['Username']:
    			blog['firstname'] = user['FirstName']
    			blog['lastname'] = user['LastName']

    options = {"blog_posts":blog_posts}
    return render_template("blog.html", **options)
