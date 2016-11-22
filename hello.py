from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!!!!!!!!!!!!'


@app.route('/index')
def index():
    url_date = {
        'site':request.args.get('chewei'),
        'num':request.args.get('num')
    }
    return render_template("index.html",url_date = url_date)

@app.route('/url/<int:post_id>')
def url_fist(post_id):
    return '你输入的数字为 %d' % post_id


@app.route('/hello/<username>')
def hello(username):
    return"欢迎你 %s" % username


@app.route('/project/')
def pro():
    return '打开网页'


@app.route('/adm')
def adm():
    return '这是网页'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
