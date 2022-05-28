from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')   
def index():
    return render_template('input.html')

@app.route('/data' ,methods = ['GET','POST'])   
def data():
    
    user_data = request.form
    print(user_data)

    name = request.form['user_name']
    print(name)
    return "Success"



if __name__ =='__main__':
    app.run(host='127.0.0.1',port=5000, debug=True)

