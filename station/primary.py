from station import app
import json
from station import db
from station.models import *
from station.calls import *

@app.route('/')
@app.route('/index')
def index():
    return json.dumps({'a' : 100, 'b' : 200})


@app.route("/users")
def user_list():
    users = User.query.all()
    userDTOs = [{'user':u.id,'username':u.username} for u in users]
    return json.dumps(userDTOs)


@app.route('/get_calls/<code>')
def calls_for_code(code):
    return json.dumps(call_data_for_code(code))

@app.route('/get_codes/')
def names_and_codes():
    return json.dumps(callers_and_codes())

@app.route('/all_calls/')
def all_call_data():
    return json.dumps(all_calls())
