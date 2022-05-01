from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
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