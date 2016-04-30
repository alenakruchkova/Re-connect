"""Models and database functions for Re-connect project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

###########################################################
# Model definitions


class Organization(db.Model):
    """List of participating organizations."""

    __tablename__ = "organizations"

    uniq_id = db.Column(db.Integer, autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    cell = db.Column(db.Integer, nullable=True)
    serves_women = db.Column(db.Boolean, nullable=True)
    serves_lgbtq = db.Column(db.Boolean, nullable=True)
    serves_minors = db.Column(db.Boolean, nullable=True)

    #Define relationship to resource
    resource = db.relationship("Resource",
                               backref=db.backref("organizations"))


class Resource(db.Model):
    """List of resources provided by organizations"""

    __tablename__ = "resources"

    uniq_id = db.Column(db.Integer, db.ForeignKey("organizations.uniq_id"),
                        nullable=False)
    emergency_housing = db.Column(db.Integer, nullable=True)
    long_term_housing = db.Column(db.Integer, nullable=True)
    counseling = db.Column(db.Boolean, nullable=True)
    career_assist = db.Column(db.Boolean, nullable=True)

    #Define relationship to organization
    organization = db.relationship("Organization", backref=db.backref("resources"))


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to Flask app."""

    # Configure to use PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///rocketmendb'  # need to change
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from app import app
    connect_to_db(app)
    print "Connected to DB."
