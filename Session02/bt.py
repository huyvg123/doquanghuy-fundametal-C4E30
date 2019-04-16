





# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, World!'
 


from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/add/<st1>/<st2>')
# def ihndex(st1,st2):
#     return str(int(st1) + int(st2)) 

@app.route('/')
def index():
  poem_data =[{
    'title':'Tĩnh dạ tứ',
    'body':'nội dung',
    'author':'Lý Bạch'
  },{
    'title':'Đồng chí',
    'body':'nội dung',
    'author':'Chính Hữu'
  }]
  return render_template('index.html',data=poem_data) 



if __name__ == '__main__':
  app.run(debug=True)

