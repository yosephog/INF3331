from temperature_co2_plotter import *
from flask import Flask, render_template, url_for, request




app=Flask(__name__)



@app.route('/')
def visualize_temprature_co2():
    return render_template('navigator.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@app.route('/handle_temperature',methods=['POST'])
def handle_temperature():
    month=request.form['month']
    year_from=int(request.form['year_from'])
    year_to=int(request.form['year_to'])
    temp_from=int(request.form['temp_from'])
    temp_to=int(request.form['temp_to'])

    plot_temprature(month,year_from,year_to,temp_from,temp_to)
    return render_template('temperature.html')

@app.route('/co2')
def co2():
    return render_template('co2.html')

@app.route('/handle_co2',methods=['POST'])
def handle_co2():
    year_from=int(request.form['year_from'])
    year_to=int(request.form['year_to'])
    plot_co2(year_from,year_to)
    return render_template('co2.html')

@app.route('/co2_by_country')
def co2_by_country():
    return render_template('co2_by_country.html')

@app.route('/handle_co2_by_country',methods=['POST'])
def handle_co2_by_country():
    year=request.form['year']
    lower_threshold=int(request.form['lower_threshold'])
    upper_threshold=int(request.form['upper_threshold'])
    plot_co2_by_country(year,lower_threshold,upper_threshold)
    return render_template('co2_by_country.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.after_request
def disable_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response
if __name__ == '__main__':
    #main_method()
    app.run(debug=True)
