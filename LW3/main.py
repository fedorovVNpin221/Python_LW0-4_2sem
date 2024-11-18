from flask import Flask, render_template, url_for

site = Flask(__name__)

@site.route('/')
def index():
    return render_template("index.html")


@site.route('/calculate', methods=['POST'])
def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + (math.sqrt(discriminant))) / (2 * a)
        x2 = (-b - (math.sqrt(discriminant))) / (2 * a)
        result = "Корни уравнения: x1 = {}, x2 = {}".format(x1, x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        result = "Уравнение имеет единственный корень: x = {}".format(x)
    else:
        result = "Уравнение не имеет действительных корней"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    site.run(debug=True)


