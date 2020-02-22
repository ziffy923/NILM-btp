import pandas as pd
import flask
from flask import Flask, render_template,jsonify, request
import pickle
import numpy as np

# load model
model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)

# routes

@app.route('/')

@app.route('/index')

def index():
    return flask.render_template('index.html')

def predict(to_predict_list):
    # get data
    # data = request.get_json(force=True)
    #
    # # convert data into dataframe
    # data.update((x, [y]) for x, y in data.items())
    # data_df = pd.DataFrame.from_dict(data)
    #
    # # predictions
    # result = model.predict(data_df)
    #
    # # send back to browser
    # output = {'results': int(result[0])}
    #
    # # return data
    # return jsonify(results=output)
    to_predict = np.array(to_predict_list).reshape(1, 4)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = model.predict(to_predict)
    return result[0]

@app.route('/result',methods=['POST'])
def results():
    if request.method =='POST':
        to_predict_list= request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int,to_predict_list))
        results = predict(to_predict_list)

        if int(results) == 1:
            prediction = 'Results is 1'
        else:
            prediction = 'Results is 0'

        return render_template("results.html", prediction=prediction)


if __name__ == '__main__':
    app.run(port = 5000, debug=True)