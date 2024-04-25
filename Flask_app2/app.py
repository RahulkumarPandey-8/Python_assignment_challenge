
#  Q2. Create a Flask app that consumes data from external APIs and displays it to users.
# Try to find an public API which will give you a data and based on that call it and deploy it on cloud platform


from flask import Flask, render_template, request
import requests # pip install requests

app = Flask(__name__) #Initialise app

# Config



@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['name']

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=20263bcee61ff9e287a139e60b814a0b'
        response = requests.get(url.format(city_name)).json()
        
        temp = response['main']['temp']
        weather = response['weather'][0]['description']
        min_temp = response['main']['temp_min']
        max_temp = response['main']['temp_max']
        icon = response['weather'][0]['icon']
        
        print(temp,weather,min_temp,max_temp,icon)
        return render_template('index.html',temp=temp,weather=weather,min_temp=min_temp,max_temp=max_temp,icon=icon, city_name = city_name)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)