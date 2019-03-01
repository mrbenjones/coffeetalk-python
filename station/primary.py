from station import app
import json
@app.route('/')
@app.route('/index')
def index():
    return json.dumps({'a' : 100, 'b' : 200})
