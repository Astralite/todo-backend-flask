from app import app
from flask import render_template, jsonify, request
from app.database import Database

db = Database("todos.db")

@app.route('/todos', methods=['GET'])
def read_all():
    try:
        result = db.get_todos()
        status = 200
    except:
        result = 'Something went wrong'
        status = 500
    return jsonify(result), status


@app.route('/todos', methods=['POST'])
def create():
    data = request.get_json()
    try:
        result = db.create_todo(data['task'], False)
        status = 201
    except:
        result = 'Something went wrong'
        status = 500
    return result, status

@app.route('/todos/<int:todo_id>', methods=['GET'])
def read_single(todo_id):
    try:
        result = db.fetch_todo_by_id(todo_id)
        status = 200
    except:
        result = 'Something went wrong'
        status = 500
    return result, status


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update(todo_id):
    data = request.get_json()
    try:
        result = db.update_todo(todo_id, data["task"], data["completed"])
        status = 200
    except:
        result = 'Something went wrong'
        status = 500
    return result, status


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete(todo_id):
    try:
        result = db.delete_todo(todo_id)
        status = 200
    except:
        result = 'Something went wrong'
        status = 500
    return result, status
