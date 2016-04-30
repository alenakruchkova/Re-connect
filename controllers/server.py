from flask import *

server = Blueprint('server', __name__, template_folder='views')

@server.route('/')
def main_route():
    """Show landing page"""

    options = {}
    return render_template("index.html", **options)


@server.route('/signup')
def signup_route():
    """Sign up page"""

    # 2.0 log in option

    options = {}
    return render_template("signup_form.html", **options)


@server.route('/home')
def home_rout():
    """Homepage with search form"""

    # 2.0 search options for geo proximity, last update

    options = {}
    return render_template("home.html", **options)


@server.route('/view_resources')
def view_resources():
    """List resources based on db query take action"""

    options = {}
    return render_template("resources.html", **options)


@server.route('/org/<int:uniq_id>')
def view_org():
    """View org info. Option to contact orgfrom page."""

    options = {}
    return render_template("org.html", **options)

# TODO
# implement results route
@server.route('/results')
def view_matches():
    """View org info. Option to contact orgfrom page."""

    options = {}
    return render_template("results.html", **options)

@server.route('/profile')
# @app.route("/profile/<int:uniq_id>")
# def show_melon(uniq_id):
def show_melon():
    """Return page showing the details of a given organization.

    Show all info about a organization. 
    Also, provide a button to contact.
    """

    return render_template("profile.html")

