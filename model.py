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
    hashed_password = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    cell = db.Column(db.Integer, nullable=True)
    serves_women = db.Column(db.Boolean, nullable=True)
    serves_lgbtq = db.Column(db.Boolean, nullable=True)
    serves_minors = db.Column(db.Boolean, nullable=True)
    emergency_housing = db.Column(db.Integer, nullable=True)
    long_term_housing = db.Column(db.Integer, nullable=True)
    counseling = db.Column(db.Boolean, nullable=True)
    career_assist = db.Column(db.Boolean, nullable=True)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to Flask app."""

    # Configure to use PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://13.88.25.31:5432/compose_postgres_1'
    db.init_app(app)


if __name__ == "__main__":

    from app import app
    connect_to_db(app)
    print "Connected to DB."
