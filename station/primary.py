from station import app
import json
from station import db
from station.models import *

@app.route('/')
@app.route('/index')
def index():
    return json.dumps({'a' : 100, 'b' : 200})


@app.route("/users")
def user_list():
    users = User.query.all()
    userDTOs = [{'user':u.id,'username':u.username} for u in users]
    return json.dumps(userDTOs)