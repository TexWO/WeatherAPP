from flask import Flask, render_template, request
import requests


app = Flask(__name__)
key = 'YOUR-API-KEY'



@app.route('/', methods=['GET', 'POST'])
def index():


    if request.method == 'POST':
        City = request.form.get('name')
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={City}&limit=1&appid={key}'

        response = requests.get(url).json()

        lat = response[0]['lat']
        lon = response[0]['lon']

        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}'
        response = requests.get(url).json()

        weather = response['weather'][0]['main']
        weather_description = response['weather'][0]['description']
        temp = response['main']['temp']
        Weather_icon = response['weather'][0]['icon']


        icon = f" https://openweathermap.org/img/wn/{Weather_icon}@2x.png"
        temp = round(temp)


        weather_data = {"weather": weather, "weather_description": weather_description, "temp": temp, "icon": icon}
        location_data = {"city": City}

        return render_template('index.html', weather=weather_data, location=location_data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0,0,0,0', port=5000, debug=True)
