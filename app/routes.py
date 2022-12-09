from app import app
from flask import render_template
from app import database as db_helper

@app.route('/')
def index():
	return render_template('index.html', name=db_helper.get_name())