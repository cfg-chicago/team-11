from flask import *
from extensions import connect_to_database

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/blog', methods=['GET', 'POST'])
def reflection_route():
    db = connect_to_database()
    cur = db.cursor()
    t = 'share'    
    cur.execute('SELECT * FROM Blog;')
    blog_posts = cur.fetchall()
    print blog_posts
    # results = cur.fetchall()
    options = {"blog_posts":blog_posts}
    return render_template("blog.html", **options)
