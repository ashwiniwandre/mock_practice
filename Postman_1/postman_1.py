import pickle
from flask import Flask, render_template,request
import numpy as np
from sklearn.utils import resample

app = Flask(__name__)

with open('scaler.pkl','rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('model.pkl','rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def predict():
    data = request.form
    print(data)

    user_data =np.zeros(3)
    user_data[0] = data['age']
    user_data[1] = data['annual']
    user_data[2] = data['score']

    scaled_user_data = scaler.transform([user_data])
    cluster = model.predict(scaled_user_data)
    print(cluster)

    return 'result done..........'

if __name__ == '__main__':
    app.run()