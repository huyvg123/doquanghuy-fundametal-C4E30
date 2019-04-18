from flask import Flask, render_template, request
app = Flask(__name__)

users_data = [{
    'user' : 'Doquanghuy1111',
    'pass' : 'doquanghuy123'  
},{
    'user' : 'Doquanghuy2222',
    'pass' : 'doquanghuy1234'
},{
    'user' : 'Doquanghuy3333',
    'pass' : 'doquanghuy12345'
}]

@app.route('/', methods=['POST'])
def login_1(): 
    print(str(request.form))
    users_user = request.form.get('Tai_Khoan')
    users_pass = request.form.get('Mat_Khau')
    users = {
        'user' : users_user,
        'pass' : users_pass
    }
    for v in users_data: 
        if users in users_data : 
            return 'Login Sussesful!'
        else :
            return 'Login Failed!' 
    users_data.append(users)
    return render_template('btvn.html',data = users_data)

@app.route('/')
def login_2():
    return render_template('btvn.html',data = users_data)

if __name__ == '__main__': 
    app.run(host= '127.0.0.1', port=5000, debug=True)