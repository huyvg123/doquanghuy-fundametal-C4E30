from flask import Flask, template_rendered
app = Flask(__name__)

@app.route('/BMI/<weight>/<height>')
def BMI(weight,height): 
    body_data = {
        'weight': weight,
        'height': height,
        'BMI': weight/((height*height)/100)
    }
    return template_rendered('BMI.html',data = body_data)
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug = True) 

