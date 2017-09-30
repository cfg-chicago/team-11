from flask import Flask, render_template
import extensions
import config
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

app.register_blueprint(controllers.main)
app.register_blueprint(controllers.reflection)
app.register_blueprint(controllers.profile)
app.register_blueprint(controllers.blog)

#check_login("doej", "12345")
# Listen on external IPs

if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)
