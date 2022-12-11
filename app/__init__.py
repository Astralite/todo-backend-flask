from flask import Flask

app = Flask(__name__)

# Make templates and static files available if you want to use them
# app = Flask(__name__, template_folder='templates', static_folder='static')

from app import routes

db = routes.db