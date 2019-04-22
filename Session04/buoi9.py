#vYaFKXSauCOe4CjC
from flask import Flask, render_template, request
from db import get_all,add_food, get_food_by_name, update
app = Flask(__name__)

@app.route('/',methods=['POST'])
def post_edit_food(name):
    food_name = request.form.get('name')
    food_price = request.form.get('price')
    update(food_name,food_price)
    return render_template('buoi9.html',data=get_all())

@app.route('/food-edit/<name>')
def edit_food(name): 
    food = get_food_by_name(name)
    return render_template('food-edit.html',food=food)

@app.route('/')
def get_food(name):
    return render_template('buoi9.html',data=get_all())


@app.route('/',methods=["POST"])
def post_food():
    food_name = request.form.get('name')
    food_price = request.form.get('price')
    food_image = request.form.get('image_url')
    add_food(food_name,food_price)

    return render_template('buoi9.html',data=get_all())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)