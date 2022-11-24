from re import S
from flask import Flask, render_template, request, redirect, send_file, make_response
from extractor.rf import extract_crop
from influx import sensor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search')
def search():
    sun = request.args.get("sun")
    temp = request.args.get("temperature")
    humid = request.args.get("humidity")
    carbon = request.args.get("CO2")
    land_moist = request.args.get("land_moist")

    crop = extract_crop(sun, temp, humid, carbon, land_moist)
    if crop == '토마토':
        return render_template("tomato.html")
    elif crop == '딸기':
        return render_template("strawberry.html")
    elif crop == '파프리카':
        return render_template("paprika.html")

@app.route('/sensor')
def get_sensor():
    sensor_data = sensor()
    sun = sensor_data[0]
    temp = sensor_data[1]
    humid = sensor_data[2]
    carbon = sensor_data[3]
    land_moist = sensor_data[4]
    rec = extract_crop(sun, temp, humid, carbon, land_moist)
    if rec == '토마토':
        return render_template("tomato.html")
    elif rec == '딸기':
        return render_template("strawberry.html")
    elif rec == '파프리카':
        return render_template("paprika.html")
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")