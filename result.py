from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'First Api'

@app.route('/fail1/<int:score>')
def fail1(score):
    return 'man is fail and marks are  ' +str(score)

@app.route('/pass1/<int:score>')
def pass1(score):
    return 'man is pass and marks are  ' +str(score)

@app.route('/success1/<int:marks>')
def success1(marks):
    if marks >=35:
        result='pass1'
    else:
        result = 'fail1'
    return redirect(url_for(result,score=marks))

if __name__ =='__main__':
    app.run()

    
    

    