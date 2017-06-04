import html

from bottle import hook, route, run, response
from core import split
from translate import GoogleTranslator


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'


@route('/')
def index():
    return dict(status='OK')


@route('/<input>')
def split_words(input):
    try:
        answer = split(input)[0]
    except IndexError:
        return dict(input=input, data=[], translations={})

    query = [input] + answer

    translator = GoogleTranslator()
    translations = translator.translate(query=query, source="is", target="en")

    response = [(source, html.unescape(translated['translatedText'])) for (source, translated) in zip(query, translations)]

    return dict(input=input, data=answer, translations=dict(response))


run(host='0.0.0.0', port=5000, debug=True)
