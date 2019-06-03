from flask import Flask, render_template, request, redirect, url_for, session
from db import get_all, add_food, get_food_by_name,update
app = Flask(__name__)
app.secret_key = 'doquanghuy9999@@@'
 
@app.route('/food-edit/<name>')
def edit_food(name):
    """
    Nhận tên món và hiển thị form sửa món ăn
    """
    food = get_food_by_name(name)
    return render_template('food-edit.html',food=food)

@app.route('/food-edit/<name>',methods=['POST'])
def post_edit_food(name):
  """
  Sửa món ăn theo tên
  """
  food_price=request.form.get('price')
  food_img=request.form.get('image_url')
  update(name,food_price,food_img)

  return redirect(url_for('get_food'))
  
@app.route('/')
def get_food():
  """
  Hiển thị các món đang có
  """
  if 'username' in session:
    return render_template('buoi9.html',data = get_all())
  else:
    return redirect(url_for('get_user'))

@app.route('/',methods=["POST"])
def post_food():
  """
  Thêm một món ăn
  """
  food_name = request.form.get('name')
  food_price = request.form.get('price')
  food_image = request.form.get('image_url')
  add_food(food_name,food_price,food_image)

  return render_template('buoi9.html',data=get_all())

@app.route('/login',methods = ["POST"])
def post_login():

    user_name = request.form.get('username')
    password = request.form.get('password')

    if user_name == 'admin' and password == 'admin':
        session['username'] = user_name
        return redirect(url_for('get_food'))
    else:
        return redirect(url_for('get_user'))

@app.route('/login')
def get_user():  
    return render_template('login.html')



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)




# from flask import Flask, render_template, request, redirect, session, url_for
# from db import get_all,add_food, get_food_by_name, update
# app = Flask(__name__)
# app.secret_key = 'asdadqwqfdafqfef123@#@'

# @app.route('/food-edit/<name>')
# def edit_food(name): 
#     """
#     Nhập tên món ăn và hiện thị form sửa món ăn
#     """
#     if 'username' in session: 
#         return render_template('food-edit.html', food=food)
#     else: 
#         return redirect(url_for('get_login'))

# @app.route('/food-edit/<name>',methods=['POST'])
# def post_edit_food(name):
#     food_name = request.form.get('name')
#     food_price = request.form.get('price')
#     update(food_name,food_price)
#     return render_template('login.html',data=get_all())

# @app.route('/')
# def get_food(name):
#     return render_template('login.html',data=get_all())


# @app.route('/',methods=["POST"])
# def post_food():
#     food_name = request.form.get('name')
#     food_price = request.form.get('price')
#     food_image = request.form.get('image_url')
#     add_food(food_name,food_price)

#     return render_template('login.html',data=get_all())

# @app.route('/login')
# def get_login():
#     return render_template('login.html')
 
# @app.route('/login', methods = ["POST"])
# def post_login():
#     user_name = request.form.get('username')
#     password = request.form.get('password')

#     if user_name == 'admin' and password == 'admin':
#         session['username'] = user_name 
#         return redirect(url_for('get_food'))
#     return redirect(url_for('get_login'))

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)




#  from flask import Flask, render_template, request
# app = Flask(__name__)

# users_data = [{
#     'user' : 'Doquanghuy1111',
#     'pass' : 'doquanghuy123'  
# },{
#     'user' : 'Doquanghuy2222',
#     'pass' : 'doquanghuy1234'
# },{
#     'user' : 'Doquanghuy3333',
#     'pass' : 'doquanghuy12345'
# }]

# @app.route('/', methods=['POST'])
# def login_1(): 
#     print(str(request.form))
#     users_user = request.form.get('Tai_Khoan')
#     users_pass = request.form.get('Mat_Khau')
#     users = {
#         'user' : users_user,
#         'pass' : users_pass
#     }
#     if users in users_data : 
#         return 'Login Sussesful!'
#     else :
#         return 'Login Failed!' 
#     users_data.append(users)
#     return render_template('login.html',data = users_data)

# @app.route('/')
# def login_2():
#     return render_template('login.html',data = users_data)

# if __name__ == '__main__': 
#     app.run(host= '127.0.0.1', port=5000, debug=True)