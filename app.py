from flask import render_template, Flask
import controllers

app = Flask(__name__, template_folder='views')
app.register_blueprint(controllers.server)
app.secret_key = open("/dev/random", "rb").read(32)
app.config['DEBUG'] = True