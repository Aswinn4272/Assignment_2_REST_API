from flask import Flask, render_template, request
import requests

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    
response = requests.get(url)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(type(data))
else:
    print(f'HTTP Request Failed with status code: {response.status_code}')


app = Flask(__name__)

@app.route('/')
def hello_world():
    result = request.args.get('name', 'temperature, windspeed, pressure')
    return render_template('index.html', result=result)

@app.route('/temp')
def temp():
    return render_template('temp.html')

@app.route('/wind_speed')
def wind():
    return render_template('wind.html')

@app.route('/pressure')
def pressure():
    return render_template('pressure.html')

# Get the temperature accordig to the date and time
@app.route('/process_temp',  methods=['post'])
def process_temp():
    date = request.form.get('date')
    time = request.form.get('time')
    
    for i in data['list']:
        if i['dt_txt'][:-3] == date +" "+ time:
            result = "Temperature = " + str(i['main']['temp'])
            break
        else:
            result = "enter a valid date time"
    
    return render_template('index.html', result=result)

# Get the wind_speed according to the date and time
@app.route('/process_wind',  methods=['post'])
def process_wind():
    date = request.form.get('date')
    time = request.form.get('time')
    
    for i in data['list']:
        if i['dt_txt'][:-3] == date +" "+ time:
            result = "wind speed = " + str(i['wind']['speed'])
            break
        else:
            result = "enter a valid date time"
    
    return render_template('index.html', result=result)


# Get the Pressure according to the date and time
@app.route('/process_pressure',  methods=['post'])
def process_pressure():
    date = request.form.get('date')
    time = request.form.get('time')
    
    for i in data['list']:
        if i['dt_txt'][:-3] == date +" "+ time:
            result = "wind speed = " + str(i['main']['pressure'])
            break
        else:
            result = "enter a valid date time"
    
    return render_template('index.html', result=result)

# to stop the app
@app.route('/terminate')
def terminate():
    return 'App terminated'


if __name__ == '__main__':
    app.run()
