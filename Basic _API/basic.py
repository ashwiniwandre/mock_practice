from flask import Flask

app = Flask(__name__)
@app.route('/')
def one():
    return 'Api done'

@app.route('/new window')
def new_window():
    return 'new tab opend'

if __name__=='__main__':
    app.run(host='127.0.0.12',port='5000',debug=True)