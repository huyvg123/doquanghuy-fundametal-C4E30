from flask import Flask, render_template, redirect,request
from db import add_bike, get_bike
app = Flask(__name__)

new_bike = [{
    'model' : 'Kids Bike',
    'daily_fee' : '500 USD',    
    'image_url' : 'https://tredz.azureedge.net/prodimg/Frog-55-20w-2019-Kids-Bike_75473_1_Supersize.jpg',
    'year' : '2019'
}]

@app.route('/')
def get_newbike():
    return render_template('btvn.html')

@app.route('/new_bike',methods = ['POST'])
def post_newbike():
    model = request.form.get('model')
    daily_fee = request.form.get('daily_fee')
    image = request.form.get('image_url')
    year = request.form.get('year') 
    add_bike(model, daily_fee, image, year)

    print(get_bike())

    return render_template('btvn.html', data = new_bike)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 