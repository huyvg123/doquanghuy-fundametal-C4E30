from flask import Flask, render_template, request, #redirect
app = Flask(__name__)

food_data = [{
        'Name':'Cơm rang',
        'Cost': '30k'
    },{
        'Name':'Gà rán',
        'Cost':'160k'
    }]

@app.route('/', methods=['POST'])
def post_food():
    print(str(request.form)) 
    food_name = request.form.get('ten_mon')
    food_gia = request.form.get('gia_tien')
    food = {
        'Name':food_name,
        'Cost':food_gia
    }
    food_data.append(food)
    return render_template('buoi8.html',data=food_data)
    #return redirect(url_for('get_food'))

@app.route('/')
def food(): 
    return render_template('buoi8.html',data=food_data)

if __name__ == '__main__': 
    app.run(host ='127.0.0.1', port=5000, debug=True)

 