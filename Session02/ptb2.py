from math import sqrt

from flask import Flask, request

app = Flask(__name__)


@app.route("/ptb2")
def tasks_manager():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    c = request.args.get('c', type=float)

    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình vô số nghiệm!"
            else:
                return "Phương trình vô nghiệm!"
        else:
            if c == 0:
                return "Phương trình có 1 nghiệm x = 0"
            else:
                return "Phương trình có 1 nghiệm x = {}".format(-c / b)
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "Phương trình vô nghiệm!"
        elif delta == 0:
            return "Phương trình có 1 nghiệm x = {}".format(-b / (2 * a))
        else:
            s = "Phương trình có 2 nghiệm phân biệt!"
            s += "<br />x1 = {}".format(float((-b - sqrt(delta)) / (2 * a)))
            s += "<br />x2 = {}".format(float((-b + sqrt(delta)) / (2 * a)))
            return s


if __name__ == '__main__':
    port = 2424
    app.run(port=port, host='127.0.0.1', threaded=True)