from flask import Flask, request, jsonify, g
from model import DBManager
from utils import str_to_datetime

DATABASE = 'worktime.db'

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = DBManager(DATABASE)
    return g.db

def valid_form_params(request):
    if 'startDate' in request.form and \
       'endDate' in request.form and \
       'category' in request.form and \
       'description' in request.form:
        return True
    return False



@app.route('/worktime', methods=['POST', 'GET'])
def insert_or_get_worktimes():
    db = get_db()
    if request.method == 'POST':
        if valid_form_params(request):
            new_id = db.insert(str_to_datetime(request.form['startDate']),
                               str_to_datetime(request.form['endDate']),
                               request.form['category'],
                               request.form['description'])
            if new_id is not None:
                return jsonify(dict(id=new_id))
            else:
                return jsonify(dict(msg='Entry could not be inserted')), 500
        else:
            return jsonify(dict(msg='Incorrect params')), 400
    else:
        start_date = request.args.get('startDate', None)
        end_date = request.args.get('endDate', None)
        if start_date is not None and end_date is not None:
            items = db.get_between(str_to_datetime(start_date), str_to_datetime(end_date))
            if items is not None:
                return jsonify(items)
            else:
                return jsonify(dict(msg='Entries could not be retrieved')), 500           
        else:
            return jsonify(dict(msg='Incorrect params')), 400

@app.route('/worktime/<id>', methods=['GET'])
def get_worktime(id):
    db = get_db()
    work_time, success = db.get(id)
    if work_time is not None:
        return jsonify(work_time)
    elif success:
        return jsonify(dict(msg='Entry not found')), 404
    else:
        return jsonify(dict(msg='Entry could not be retrieved')), 500


@app.route('/worktime/<id>', methods=['PUT'])
def update_worktime(id):
    db = get_db()
    if valid_form_params(request):
        result = db.update(id,
                  str_to_datetime(request.form['startDate']),
                  str_to_datetime(request.form['endDate']),
                  request.form['category'],
                  request.form['description'])
        if result is not None and result > 0:
            return jsonify(dict(id=id))
        elif result is not None and result == 0:
            return jsonify(dict(msg='Entry not found')), 404
        else:
            return jsonify(dict(msg='Entry could not be updated')), 500
    else:
        return jsonify(dict(msg='Incorrect params')), 400


@app.route('/worktime/<id>', methods=['DELETE'])
def delete_worktime(id):
    db = get_db()
    result = db.delete(id)
    if result is not None and result > 0:
        return jsonify(dict(id=id))
    elif result is not None and result == 0:
        return jsonify(dict(msg='Entry not found')), 404
    else:
        return jsonify(dict(msg='Entry could not be removed')), 500

if __name__ == '__main__':
    app.run()
    
