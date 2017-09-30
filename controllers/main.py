from flask import *

from extensions import connect_to_database

main = Blueprint('main', __name__, template_folder='templates')

def import_text_file(filename):
	return open(filename, "r")

@main.route('/')
def main_hello():
    # db = connect_to_database()
    # cur = db.cursor()
    # create_table_queries = open("create_tables.sql", "r")
    # cur.execute(create_table_queries)
    # results = cur.fetchall()
    return 'Hello world'
    #return render_template("index.html")