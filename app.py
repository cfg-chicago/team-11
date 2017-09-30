from flask import Flask, render_template
import extensions
import config

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

<<<<<<< HEAD
app.register_blueprint(controllers.main)


# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)
=======
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
	app.run(host='0.0.0.0')
>>>>>>> ec1f074ffa999202958c832a952e51e65984845b
