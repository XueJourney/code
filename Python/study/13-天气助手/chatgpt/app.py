import requests
from flask import Flask, render_template, request
import uuid

shared_results = {}

app = Flask(__name__)

def get_weather(city):
    url = f"https://www.tianqiapi.com/api/?version=v6&appid=74169348&appsecret=ti3VzXtb&city={city}"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        share_id = str(uuid.uuid4())  # 生成唯一的分享ID
        shared_results[share_id] = weather_data  # 将分享ID与天气查询结果关联存储
        return render_template("index.html", weather_data=weather_data, share_id=share_id)
    return render_template("index.html")

@app.route('/share/<share_id>')
def share(share_id):
    weather_data = shared_results.get(share_id)
    if weather_data:
        return render_template("share.html", weather_data=weather_data)
    else:
        return "Invalid share link."

if __name__ == "__main__":
    app.run()