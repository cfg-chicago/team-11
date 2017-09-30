from flask import Flask, render_template
import extensions
import config

# Initialize Flask app with the template folder address
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
