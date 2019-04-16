from flask import Flask, template_rendered
app = Flask(__name__)

@app.route('/user/<username>')
def user(username): 
    users_data = [{
        'name':'Do Quang Huy',
        'work':'student',
        'school':'Thuyloi university',
        'hobbies':'listen to music, play a game, technology, ...'
    },{
        'name':'Dang Van Phi',
        'work':'student',
        'school':'national economic university',
        'hobbies':'play a game, learning english,...'
    }
    return template_rendered('users.html',data = users_data)
if __name__ == '__main': 
    app.run(host='127.0.0.1',port=5000,debug=True)
