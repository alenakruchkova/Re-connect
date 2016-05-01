from flask import *
from twilio.rest import TwilioRestClient
import twilio.twiml

account_sid = "AC8f9b5a52430b59c4275e1a9b8bc7a78a"
auth_token = "d78c7e970a38a975aa3e229d5700957c"
client = TwilioRestClient(account_sid, auth_token)

server = Blueprint('server', __name__, template_folder='views')

 
@server.route("/voice", methods=['GET', 'POST'])
def hello_monkey():
    """Send an sms booking request."""

    callers = [
         "+18087561115",
         "+14155168977",
         "+16264371554",
         "+16143298370",
         "+16508614833",
    ]

    for i in callers:
        client.messages.create(
        to=i,
        from_="+12065390536",
        body="Request for emergency housing.",
        media_url="https://0.s3.envato.com/files/106594784/Images.jpg",
    )

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/results")

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
@server.route('/donors')
def message_to_donors():
    """Message to donors"""

    options = {}
    return render_template("donors.html", **options)


@server.route('/signup', methods=['POST'])
def signup_process():
    """Process signup registration."""
    #get form variables here
    email = request.form["email"]
    hashed_password = request.form["hashed_password"]

    new_organization = Organization()

    db.session.add(new_organization)
    db.session.commit()
    set_login_session(new_organization)
    flash("%s added!" % email)

    return redirect('/home')

@server.route('/home')
def home_route():
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


# @app.route('/send-email', methods=['POST'])
# def send_email():
#     """Flask Mail app route."""
#     email = request.form.get('email')

#     msg = Message(
#           'Human Trafficking Institutions with Available Resources',
#           sender='athackhackathon@gmail.com',
#           recipients=[email])
#     msg.html = body

#     mail.send(msg)

#     flash('Email has been sent!')

#     return redirect('/')

#log in function:
def set_login_session(user):
    session["uniq_id"] = organization.uniq_id
    session['email'] = organization.email
    session['hashed_password'] = organization.hashed_password

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
def show_profile():
    """Return page showing the details of a given organization.

    Show all info about a organization.
    Also, provide a button to contact.
    """

    return render_template("profile.html")

    options = {}
    return render_template("org.html", **options)


@server.route('/results')
def show_companylist():
    """Return page showing a list of companies with contact buttons."""

    return render_template("results.html")
