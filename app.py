import pandas as pd
import flask
from flask import Flask, render_template,jsonify, request
import pickle,gzip
import json

import numpy as np
# from keras.models import load_model
# import h5py
#
# prd_model = load_model('model-rc.hdf5')

# model = pickle.load(open('decision_tree_model.pkl','rb'))

model2 = pickle.load(gzip.open('dst_refree.pklz', 'rb'))

model_ds_all  = pickle.load((gzip.open('ds_model_all_new.pklz','rb')))

appliance_list = ['oven_3', 'oven_4', 'dishwaser_6', 'kitchen_outlets_7', 'kitchen_outlets_8', 'lighting_9', 'washer_dryer_10', 'microwave_11', 'bathroom_gfi_12', 'electric_heat_13', 'stove_14', 'kitchen_outlets_15', 'kitchen_outlets_16', 'lighting_17', 'lighting_18', 'washer_dryer_19', 'washer_dryer_20']

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

app = Flask(__name__)

@app.route('/')

@app.route('/index')
def index():
    return flask.render_template('new_html.html')

def predict(to_predict_list):
    # get data
    # data = request.get_json(force=True)
    #
    # convert data into dataframe
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

    to_predict = np.array(to_predict_list).reshape(1, 2)
    # loaded_model = pickle.load(open("ds_model_all.pkl", "rb"))
    output_appliance = {}
    for app,i in zip(appliance_list,range(20)):
        # output_appliance[app] = "".join(str(len(model_ds_all[i].predict(to_predict))))
        output_appliance[app] = format(model_ds_all[i].predict(to_predict))

        # output_appliance.append(model_ds_all[i].predict(to_predict))
    # k = (json.dumps(output_appliance,cls=NumpyEncoder))

    return (output_appliance)

@app.route('/result',methods=['POST'])
def results():

    if request.method =='POST':

        to_predict_list= request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int,to_predict_list))
        results = predict(to_predict_list)
        print(results)
        print(results['oven_3'])
        return render_template("results.html", prediction=results)

def format(value):
    return "%.3f" % value


if __name__ == '__main__':
    app.run(port = 5000, debug=True)