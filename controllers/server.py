from flask import *

server = Blueprint('server', __name__, template_folder='views')

@server.route('/')
def main_route():
    options = {}
    return render_template("index.html", **options)

@server.route('/signup')
def signup_route():
	options = {}
	return render_template("signup_form.html", **options)