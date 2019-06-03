from flask import Flask, template_rendered, redirect
app = Flask(__name__)

@app.route('/about_me')
def about_me(): 
    infomation_data = [{
        'information':'Thong Tin: ',
        'name':"Do Quang Huy",
        'work':'student',
        'school':'Thuyloi university',
        'hobbies':'listen to music, play a game, technology, ...'
    }]
    return template_rendered('abuot_me.html',data = infomation_data)

@app.route('/school')
def school(): 
    return redirectx(' http://techkids.vn ')

if __name__ == '__main__' : 
    app.run(host='127.0.0.1',port=5000,debug=True)
