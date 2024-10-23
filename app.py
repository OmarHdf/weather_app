from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '94c9ebe34e759a3e8f6e4e7806e25b02'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    weather_data = response.json()

    if weather_data.get('cod') != 200:
        message = weather_data.get('message', 'Erreur lors de la récupération des données.')
        return render_template('result.html', error=message)

    return render_template('result.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
