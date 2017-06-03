from bottle import route, run, template, response
from core import split

@route('/split/<input>')
def index(input):
    return dict(data=split(input))

run(host='0.0.0.0', port=3000, debug=True)
