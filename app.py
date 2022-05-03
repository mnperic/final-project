from flask import Flask, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/predict',methods=['POST'])
def predict():

    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)
    #output = np.round(prediction[0], 2)

    return render_template('index.html')

#@app.route('/results',methods=['POST'])
#def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

@app.route('/visualisation')
def visualisation():
    return render_template('index.html')

@app.route('/fueltype')
def fueltype():
    return render_template('fueltype.html')

@app.route('/energybystate')
def energybystate():
    return render_template('energybystate.html')

@app.route('/evsales')
def evsales():
    return render_template('evsales.html')

@app.route('/globaltempincrease')
def globaltempincrease():
    return render_template('globaltempincrease.html')

@app.route('/evsalesforecast')
def evsalesforecast():
    return render_template('evsalesforecast.html')

@app.route('/crudeoilforecast')
def crudeoilforecast():
    return render_template('crudeoilforecast.html')

@app.route('/globaltempforecast')
def globaltempforecast():
    return render_template('globaltempforecast.html')

@app.route('/lithiumforecast')
def lithiumforecast():
    return render_template('lithiumforecast.html')

@app.route('/coalforecast')
def coalforecast():
    return render_template('coalforecast.html')

@app.route('/co2emissionforecast')
def co2emissionforecast():
    return render_template('co2emissionforecast.html')

@app.route('/Forecasts')
def Forecasts():
    return render_template('Forecasts.html')

@app.route('/MLpredictions')
def MLpredictions():
    return render_template('MLpredictions.html')

    
if __name__ == '__main__':
    app.run(debug=True)