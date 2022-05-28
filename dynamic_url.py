from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def one():
    return 'Api done'

@my_app.route('/admin/<name>')
def admin(name):
    return 'admin is = '+name

@my_app.route('/value/<int:num>')
def value(num):
    return 'num is  ='+str(num)


if __name__=='__main__':
    my_app.run()