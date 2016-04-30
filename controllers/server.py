from flask import *

server = Blueprint('server', __name__, template_folder='views')

@server.route('/')
def main_route():
    options = {}
    return render_template("index.html", **options)
