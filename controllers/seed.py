"""Utility file to seed Re-connect database with demo data"""

from model import Organization
from model import Resource

from model import connect_to_db, db
from app import app

##############################################################


def load_organizations():
    """Load information from test_data.csv into database"""

    print "Orgs"

    # Delete all rows in Organization table, so if we need to run this script a second time,
    # we won't be trying to add duplicate users
    Organization.query.delete()

    # Read test_data.csv file
    for row in open("seed_data/test_data.csv"):
        r = row.splitlines()

        for rn in r:
            name, address, email, phone, cell, serves_women, serves_lgbtq, serves_minors, emergency_housing, long_term_housing, counseling, career_assist = rn.split(",")

            serves_women = serves_women or False
            serves_lgbtq = serves_lgbtq or False
            serves_minors = serves_minors or False
            emergency_housing = emergency_housing or False
            long_term_housing = long_term_housing or False
            counseling = counseling or False
            career_assist = career_assist or False

            organization = Organization(name=name,
                              address=address,
                              email=email,
                              phone=phone,
                              cell=cell,
                              serves_women=serves_women,
                              serves_lgbtq=serves_lgbtq,
                              serves_minors=serves_minors,
                              emergency_housing = emergency_housing,
                              long_term_housing = long_term_housing,
                              counseling = counseling,
                              career_assist = career_assist)

            # add to the session
            db.session.add(organization)

        # commit
        db.session.commit()

 ####################################################

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import data
    load_organizations()
