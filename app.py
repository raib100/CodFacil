from flask import Flask, render_template


app = Flask(__name__)


@app.route('/index/<name>')
def index(name='Ricardo'):
    MiLista = [1,2,3,4,5]
    edad = 56
    return render_template('index.html', name=name, edad=edad, lista=MiLista)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
