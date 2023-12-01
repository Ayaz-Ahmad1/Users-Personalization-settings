# app.py
from flask import Flask
from models import db
import os
from dotenv import load_dotenv
from views import configure_routes
load_dotenv()

# Database connection details
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{host}/{db_name}'
db.init_app(app)

# Configure routes
configure_routes(app)

# Run the Flask app in debug mode
if __name__ == '__main__':
    with app.app_context():
        # Create all database tables
        db.create_all()
    app.run(debug=True)
