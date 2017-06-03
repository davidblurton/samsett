from bottle import route, run
from core import split


@route('/')
def index():
    return dict(status='OK')


@route('/<input>')
def split_words(input):
    return dict(data=split(input))


run(host='0.0.0.0', port=3000, debug=True)
