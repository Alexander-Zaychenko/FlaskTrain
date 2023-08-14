from flask import Flask, redirect, render_template
import os

app = Flask(__name__)

# make dynamic page


@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/home', code=302)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/fun')
def fun():
    return render_template('fun.html')


@app.route('/home/branch')
def branch():
    return render_template('branch.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
